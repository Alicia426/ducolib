# DUCOlib: A friendly Duino-Coin Python Library.

DUCOlib strives to be the most accesible miner and mining library for [Duino-Coin](https://duinocoin.com/)
within the Python ecosystem. 

Written in pure Python, `ducolib` lets us implement Duino-Coin mining in an easy and straightforward way.


## Installation:

Simply run `pip install ducolib`.

If you would like to install manually, please clone this repository, 
then run `python setup.py install`.

This module has no install dependencies and is made to run with the Python standard library.


## Usage:

DUCOlib is friendly for users and developer, it can be imported as any other python module, 
or used to mine through a simple CLI.

### As a library:


Let's start with an example:

```python
import ducolib
import time

# Parameters for constructor:   Username   Diff, Threads, rig name.
workers=ducolib.MinerCrewChief('Alicia426' ,True ,'auto' ,'myrig')

workers.start_mining() # Starts all mining threads.
time.sleep(30) # Mining for 30 seconds
workers.stop_mining() # Stops all threads.

```

As we can see, the `MinerCrewChief` class orchestrates all mining, this is done
through the `Miner` class. 



### As a CLI Miner:

As a miner `ducolib` takes 1 mandatory argument, the `username`
like so: `ducolib Alicia426`, any other arguments are optional.

The full list of arguments, in order:

1. Username - DUCO username, required. 
2. Mining Difficulty - `easy` for lower difficulty, `net` for network difficulty. Optional, defaults to Network.
3. Threads - Number of desired threads, either a number or `auto` which mines on all threads. Optional, defaults to `auto`.
4. Rig name - Mining rig name, Optional, defaults to `Ducolib`.
5. Session duration - Mining session length in hours, Optional, defaults to 8 hours.

Some command exammples:

* `ducolib Alicia426 easy auto MyRig 24`
* `ducolib Alicia426 net 1`


**You will not see any console output, that is by design**, however
the log file `ducolib.log` should be present in your working directory.

It might look a bit like this:

```log
2021-03-31 00:25:44,839 -> INFO :: Mining DUCO for Alicia426 with Glukhov Miner :)
2021-03-31 00:25:44,839 -> INFO :: Using Lower Mining Difficulty: True. On rig: Yagentci
2021-03-31 00:25:44,839 -> INFO :: No previously running threads, OK!
2021-03-31 00:25:44,845 -> INFO :: Mining Started on Thread 0!
2021-03-31 00:25:44,845 -> INFO :: No previously running threads, OK!
2021-03-31 00:25:44,848 -> INFO :: Mining Started on Thread 1!
2021-03-31 00:25:45,652 -> INFO :: Server is on version: 2.3
2021-03-31 00:25:45,661 -> INFO :: Server is on version: 2.3
2021-03-31 00:26:02,964 -> INFO :: Accepted share: 2948235 Difficulty: 30000
2021-03-31 00:26:02,972 -> INFO :: Accepted share: 2914617 Difficulty: 30000
2021-03-31 00:26:05,652 -> INFO :: Accepted share: 508330 Difficulty: 9583
2021-03-31 00:26:05,702 -> INFO :: Accepted share: 439376 Difficulty: 9585
2021-03-31 00:26:07,553 -> INFO :: Accepted share: 376336 Difficulty: 14300
2021-03-31 00:26:09,142 -> INFO :: Accepted share: 852332 Difficulty: 14430
2021-03-31 00:26:09,602 -> INFO :: Accepted share: 5410 Difficulty: 19445
```

## Changelog:

* Started project.
* Tested PyPI packaging.
* Added way to check in on miners.
* Built CLI.
* Filled in documentation.
* Fixed major disconnect bug. 
* Updated documentation.