"""
ftp  文件服务器，服务端
env : python3.6
多进程／线程并发　 socket
"""

from socket import *
from threading import Thread
import sys,os
import time


#全局变量
ADDR = ('127.0.0.1',7878)
FTP = '/home/tarena/FTP/'  #文件库的绝对位置(切记：绝对路径前后都有／)

#创建类实现服务器文件处理功能
class FTPServer(Thread):
    """
    查看列表，下载，上传，退出处理
    """
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__()

    #查看文件列表
    def do_list(self):

        files = os.listdir(FTP) #获取文件列表
        if not files:
            self.connfd.send('文件库为空'.encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1) #隔一点，以防粘包

        #拼接文件
        filelist = ""
        for i in files:    #遍历文件夹中的每个不是隐藏属性的文件进行拼接发送
            if i[0] != '.' and \
                   os.path.isfile(FTP+i): #判断是否是普通文件，隐藏前面有.且判断路径加文件的对象是否为文件
                filelist += i + '\n' #将那个普通文件再进行拼接发送
        self.connfd.send(filelist.encode())

    #下载文件
    def do_get(self,filename):
        try:
            f = open(FTP + filename,'rb') #路径加文件名可以找到路径'/home/tarena/FTP/文件名'
        except Exception:
            #打开失败文件不存在
            self.connfd.send("文件不存在".encode())
            return
        else:
            self.connfd.send(b'OK')
            time.sleep(0.1) #以防与内容粘包

        #发送文件
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    #上传文件
    def do_put(self,files):
        if os.path.exists(FTP + files):  #判断此文件是否存在
            self.connfd.send('该文件已存在'.encode())
            return
        else:
            self.connfd.send(b'OK')


        f = open(FTP + files,'wb')
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break

            f.write(data)
        f.close()


    #循环接收请求，分情况调用功能函数
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if not data or data == 'Q':
                return  #结束run（线程随之结束）
            elif data == 'L':
                self.do_list()
            elif data[0] == 'G':
                filename = data.split(' ')[-1]
                self.do_get(filename)
            elif data[0] == 'P':
                files = data.split(' ')[-1]
                self.do_put(files)


def connects(s):
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue

        #创建线程处理请求
        client = FTPServer(c)
        client.setDaemon(True) #父进程则所有服务终止（父退出自动结束子）
        client.start()  #运行run,线程开始


#搭建网络服务端模型
def main():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)
    print("Listen the port 7878")
    connects(s)


if __name__ == '__main__':
    main()



