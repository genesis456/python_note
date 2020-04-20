"""
获取进程PID号
"""
import os
from time import sleep
pid = os.fork()

if pid < 0:
    print("Error")
elif pid ==0:
    sleep(1)
    print("Child PID:",os.getpid())  #获取本（子）进程PID
    print("Get parent PID:",os.getppid())  #子进程中获取父进程的PID
else:
    print("Get child PID:",pid)  #父进程中获取自己的PID，子进程的返回值就是父进程的PID
    print("Parent PID:",os.getpid()) #获取子PID


#建议终端运行
#父进程先执行完退出，留下子进程（孤儿进程），
# 操作系统会自动将子进程分配给新的父进程（养父）
#所以运行时，可以看到父进程的PID不一样，但（养父）的pid都是一样的