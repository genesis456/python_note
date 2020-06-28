"""
thread1.py  线程基础使用
步骤：   基本同Process
        1、封装线程函数
        2、创建线程对象
        3、启动线程
        4、回收线程
"""
import threading
from time import sleep
import os


def music1():
    for i in range(3):
        sleep(1)
        print(os.getpid(),"播放：安河桥")

def music2():
    for i in range(3):
        sleep(1)
        print(os.getpid(),"播放：斑马斑马")
def main():
    #创建线程对象
    t1 = threading.Thread(target = music1)
    t2 = threading.Thread(target=music2)
    t1.start()#启动线程
    t2.start()
    t1.join()#回收线程
    t2.join()

if __name__ == '__main__':
    main()