import ducolib
import time

# Mining for 30 seconds
workers=ducolib.MinerCrewChief('Alicia426',True,'auto','red')
workers.start_mining()
time.sleep(1000)
print(workers.check_status())
time.sleep(1000)
print(workers.check_status())
workers.stop_mining()
