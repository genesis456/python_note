#多线程

from test import *
from threading import Thread
import time

jobs = []
tm = time.time()
for i in range(10):
    # p = Thread(target=count, args=(1,1))
    p = Thread(target=io)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()
print("Tread cpu:",time.time() - tm)