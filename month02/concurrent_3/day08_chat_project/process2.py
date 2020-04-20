"""
multiprocessing  创建多个进程
"""

import multiprocessing as mp
from time import sleep
import os

def th1():
    sleep(2)
    print("吃饭")
    print(os.getppid(),'--',os.getpid())


def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(), '--', os.getpid())
def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), '--', os.getpid())

things = [th1,th2,th2]
jobs = []
for th in things:
    p = mp.Process(target = th)
    jobs.append(p)  #将进程对象保存
    p.start()

#一起回收
for i in jobs:
    i.join()