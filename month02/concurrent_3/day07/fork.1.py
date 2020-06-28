"""
fork1.py fork进程演示细节
"""

import os
from time import sleep
#子进程只会在创建fork的下一句开始运行
print("===========")
a= 1  #会占内存的（子进程都会copy）
#创建子进程
def fun():
    print("fun .... ")

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    print("Child process")
    print("a = ",a)  # 从父进程空间拷贝了变量
    fun()
    a = 10000  #改的是子进程的a，不会影响父进程#，只是修改了自己空间的a
else:
    sleep(1)
    print("Parent process")
    print("a:",a)

print("All a ->",a)