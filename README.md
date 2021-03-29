# DUCOlib: A friendly Duino-Coin Python Library.

DUCOlib strives to be the most accesible miner and mining library for [Duino-Coin](https://duinocoin.com/)
within the Python ecosystem. 

Written in pure Python, `ducolib` lets us implement Duino-Coin mining in an easy and straightforward way.


## Installation:

Simply run `pip install ducolib`.

If you would like to install manually, please clone this repository, 
then run `python setup.py install`.


## Usage:

DUCOlib is friendly for users and developer, it can be imported as any other pyuthon module, 
or used to mine through a simple CLI.

### As a library:



Here is an example:

```python
import ducolib
import time

# Mining for 30 seconds
workers=ducolib.MinerCrewChief('Alicia426',True,'auto')

workers.start_mining()
time.sleep(30)
print(workers.check_status())
time.sleep(1000)
print(workers.check_status())
workers.stop_mining()

```

### As a CLI Miner:


## Changelog:

* Started project.
* Tested PyPI packaging.
* Added way to check in on miners.
* Built CLI.
* Filled in documentation.