"""
signal_.py
#处理僵尸进程方法3
信号处理僵尸
"""
import os,sys
import signal

#一定要在创建子进程之前发送信号
#子进程退出时父进程忽略退出行为，子进程由操作系统处理
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid ==0:
    print("Child PID:",os.getpid())#打印自己的PID
    sys.exit("子进程退出") #若参数写2，退出状态为512
else:

    while True:  #父进程不退出
        pass

#处理僵尸的程序运行完，到终端ps -aux查看进程的信息，
# 看运行的那个进程还在不在，若不在则处理成功