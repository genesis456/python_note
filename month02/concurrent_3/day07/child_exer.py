#练习
"""
child.py
#处理僵尸进程方法2（创建二级子进程）：
#将下列事件同时运行
def f1():
    for i in range(3):
        sleep(2)
        print("写 代码")

def f2():
    for i in range(2):
        sleep(4)
        print("测代码")
"""
from time import sleep
import os

def f1():
    for i in range(3):
        sleep(2)
        print("写代码")

def f2():
    for i in range(2):
        sleep(4)
        print("测代码")

pid = os.fork()
if pid <0:
    print("Error")
elif pid == 0:   #一级子进程
    pid2 = os.fork()
    if pid2 <0:
        print("Error")
    elif pid2 ==0:  #二级子进程
        f1()
    else:   #二级子进程的父进程（一级子进程）
        os._exit(0)  #创建二级子进程一级就同时退出，
else:  #父进程
    os.wait()  #等一级子进程退出同时并处理(以防僵尸进程)
    f2()

#运行发现是同时运行的