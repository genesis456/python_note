"""
dict服务端
功能：业务逻辑处理
模型：tcp,多进程　Process
"""

from socket import *
from multiprocessing import Process
import signal  #处理僵尸进程


#全局变量
HOST = '0.0.0.0'
PORT = 5454
ADDR = (HOST,PORT)

def handle(c):
    #循环接收客户端发送来的请求
    data = c.recv(1024).decode()
    print(c.getpeername(),':',data)



#搭建网络
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    print("Listen the Port 5454...")
    #循环等待客户端连接
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:  #ctrl+c
            s.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue

        #有客户端连接进来
        p = Process(target=handle,args=(c,))
        p.daemon = True   #父进程退出，子进程随之退出
        p.start()



if __name__ == '__main__':
    main()


