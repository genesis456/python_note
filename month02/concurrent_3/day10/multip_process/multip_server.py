"""
作者：周乐
日期：2020/3/29
multip_server.py 基于process的多进程并发
(采用tcp)
1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接
5. 如果客户端退出，则销毁对应的进程

"""
from socket import *
from multiprocessing import Process
import os,signal

HOST = '0.0.0.0'
PORT = 5454
ADDR = (HOST,PORT)

def handle(c):
    # s.close()
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b'OK')
    c.close()
    os._exit(0)


def connector(s):
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            os._exit(0)
        except Exception as e:
            print(e)
            continue

        p1 = Process(target=handle, args=(c))
        p1.daemon = True #父进程则所有服务终止（父退出自动结束子）
        p1.start()
        # p1.join()#不能用join阻塞在此,做完子才能继续循环（Ｘ）
        c.close()


def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #设置端口重用
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    print("Listen the port 5454...")
    connector(s)


if __name__ == '__main__':
    main()