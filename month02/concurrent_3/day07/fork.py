"""
fork.py  fork进程创建演示

程序本身运行都会产生一个进程，用fork可以创建一个子进程
"""
import os

pid = os.fork()

if pid < 0:   #pid是系统为每个进程分配的标识．小于０说明创建失败
    print("Create process failed")
#子进程执行部分
elif pid == 0:
    print("The new process")

#父进程执行部分
else:
    print("The old process")
#父子进程都会执行
print("Fork test over")

#父子进程各自独立运行，运行顺序不一定
#pycharm 内部优化，有时候可能会只执行父进程，丢失子进程