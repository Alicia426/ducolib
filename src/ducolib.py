#!/usr/bin/env python3

import socket
import hashlib
import urllib.request
import time
import os
import logging
import sys
import multiprocessing

logging.basicConfig(filename='ducolib.log', level=logging.DEBUG,
                    format='%(asctime)s -> %(levelname)s :: %(message)s')


class Miner:

    def __init__(self, username, UseLowerDiff):
        self.username = username
        self.UseLowerDiff = UseLowerDiff
        self.soc = socket.socket()
        self.soc.settimeout(15)

    def mine(self):
        current_buffer = ''
        if self.UseLowerDiff:
            self.soc.send(
                bytes("JOB," + str(self.username) + ",MEDIUM", encoding="utf8")
            )  # Send job request for lower difficulty
        else:
            self.soc.send(
                bytes("JOB," + str(self.username), encoding="utf8")
            )  # Send job request
        job = self.soc.recv(1024).decode()  # Get work from pool
        # Split received data to job (job and difficulty)
        job = job.split(",")
        difficulty = job[2]

        # Calculate hash with difficulty
        for result in range(100 * int(difficulty) + 1):
            ducos1 = hashlib.sha1(
                str(job[0] + str(result)).encode("utf-8")
            ).hexdigest()  # Generate hash
            if job[1] == ducos1:  # If result is even with job
                self.soc.send(
                    bytes(str(result) + ",,Minimal_PC_Miner", encoding="utf8")
                )  # Send result of hashing algorithm to pool
                # Get feedback about the result
                feedback = self.soc.recv(1024).decode()
                if feedback == "GOOD":  # If result was good
                    current_buffer = "Accepted share: " + \
                        str(result)+' '+"Difficulty: "+str(difficulty)
                    break
                elif feedback == "BAD":  # If result was bad
                    current_buffer = "Rejected share: " + \
                        str(result)+' '+"Difficulty: "+str(difficulty)
                    break
        return current_buffer

    def requestAndMine(self):
        while True:
            try:
                # This sections grabs pool adress and port from Duino-Coin GitHub file
                serverip = "https://raw.githubusercontent.com/revoxhere/duino-coin/gh-pages/serverip.txt"  # Serverip file
                with urllib.request.urlopen(serverip) as content:
                    content = (
                        content.read().decode().splitlines()
                    )  # Read content and split into lines
                pool_address = content[0]  # Line 1 = pool address
                pool_port = content[1]  # Line 2 = pool port

                # This section connects and logs user to the server
                # Connect to the server
                self.soc.connect((str(pool_address), int(pool_port)))
                server_version = self.soc.recv(
                    3).decode()  # Get server version
                logging.info("Server is on version: "+str(server_version))
                # Mining section
                while True:
                    buff = self.mine()
                    if 'Accepted' in buff:
                        logging.info(buff)
                    elif 'Rejected' in buff:
                        logging.warning(buff)
                    else:
                        logging.warning('Empty buffer, likely error')

            except Exception as e:
                logging.error("Error occured: " + str(e) +
                              ", restarting in 5s.")
                time.sleep(5)
                try:
                    self.soc.close()
                except Exception as e:
                    logging.warning(str(e))

    def start_mining(self):
        """Starts mining as a process"""
        try:
            self.proc.terminate()  # pylint: disable=access-member-before-definition
        except Exception:
            logging.info('No previously running threads, OK!')
        finally:
            self.proc = multiprocessing.Process(  # pylint: disable=attribute-defined-outside-init
                target=self.requestAndMine, args=())
            self.proc.start()

    def stop_mining(self):
        """Stops mining as a process"""
        try:
            self.proc.terminate()  # pylint: disable=access-member-before-definition
        except Exception as e:
            logging.error(str(e))

    def check_status(self):
        """Returs a copy of the current mine() method buffer."""
        with open('ducolib.log') as f:
            return f.readlines()[-1]


class MinerCrewChief:

    def __init__(self, username, UseLowerDiff, threads):

        self.miners = []
        self.username = username
        self.UseLowerDiff = UseLowerDiff
        self.threads = threads
        logging.info('Mining DUCO for {}'.format(self.username))
        logging.info('Using Lower Mining Difficulty: '+str(self.UseLowerDiff))

    def start_mining(self):
        if self.threads == 'auto':
            self.threads = os.cpu_count()
        for i in range(self.threads):
            m = Miner(self.username, self.UseLowerDiff)
            m.start_mining()
            logging.info('Mining Started on Thread {}!'.format(i))
            self.miners.append(m)

    def stop_mining(self):
        try:
            csr = 0
            for m in self.miners:
                m.stop_mining()
                logging.info('Mining thread {} stopped!'.format(csr))
                csr += 1

        except NameError:
            logging.warning('Tried stopping non existent miners.')

    def check_status(self):
        """For every miner:
        returs a copy of the current mine() method buffer."""
        states=[]
        try:
            for m in self.miners:
                s=m.check_status()
                s=s.strip()
                states.append(s)

        except NameError:
            logging.warning('Tried checking non existent miners.')

        return states

if __name__ == "__main__":
    #workers = MinerCrewChief('Alicia426', True, 'auto')
    workers = MinerCrewChief('Alicia426', False, 'auto')
    workers.start_mining()
    time.sleep(500)
    workers.stop_mining()
