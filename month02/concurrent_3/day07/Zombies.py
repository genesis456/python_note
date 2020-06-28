"""
模拟僵尸进程产生
子进程比父进程先行退出
"""
import os,sys

pid = os.fork()
if pid < 0:
    print("Error")
elif pid ==0:
    print("Child PID:",os.getpid())#打印自己的PID
    sys.exit("子进程退出") #若参数写2，退出状态为512
else:
    """
    os.wait()  处理僵尸进程方法1
    """
    #pid退出的子进程PID，status子进程退出状态
    pid,status = os.wait()
    print("pid:",pid)
    print("statis:",status) #child 退出状态 *256

    while True:  #父进程不退出
        pass

#这种单独处理僵尸进程的方法有缺陷：要子进程执行完才到父进程。没有做到并行同时运行