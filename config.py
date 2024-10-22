import os
from pathlib import Path
from itertools import cycle
from utils.helpers import read_txt

CWD = os.getcwd()
ADDRESSES = read_txt(os.path.join(CWD, Path("data/addresses.txt")))
PROXIES = read_txt(filename=os.path.join(CWD, Path("data/proxies.txt")))
PROXY_CYCLE = cycle(PROXIES)
