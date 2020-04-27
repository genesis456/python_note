"""
dict 客户端
根据客户端的输入，发送不同的请求
一级界面：　注册　，登录，退出
二级界面：　查单词，历史记录，注销
"""
from socket import *
import getpass

#全局变量
ADDR = ('0.0.0.0',5454)
s = socket()
s.connect(ADDR)

def register():
    user = input("user:")
    passpwd = getpass.getpass()
    msg = "H %s %s" % (user,passpwd)
    s.send(msg.encode())
    data = s.recv(1024).decode()
    if data == 'OK':
        print("注册成功")
    else:
        print(data)

def main():
    while True:
        print("""==================
            　　　1.注册　2登录　3.退出
                 ==================""")
        cmd = input("输入命令：")
        if cmd == '1':
            register()
        elif cmd == '2':
            pass
        elif cmd == '3':
            pass
        else:
            print("请输入正确命令")

if __name__ == '__main__':
    main()



"""
模拟网站的后端应用

从httpserver接收具体请求
根据请求获取网页
将需要的数据反馈给httpserver
"""

from socket import *
import json
from settings import *
from select import *
from urls import *

# 应用类,实现具体的后端功能
class Application:
    def __init__(self):
        self.host = frame_ip
        self.port = frame_port
        self.fdmap = {} # 查找地图
        self.ep = epoll() # epoll对象
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,
                               SO_REUSEADDR,
                               DEBUG)
        self.sockfd.bind((self.host,self.port))

    # 用于服务启动
    def start(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        # 关注sockfd
        self.ep.register(self.sockfd,EPOLLIN)
        self.fdmap[self.sockfd.fileno()] = self.sockfd

        while True:
            events = self.ep.poll()
            for fd,event in events:
                if fd == self.sockfd.fileno():
                    connfd,addr = self.fdmap[fd].accept()
                    self.ep.register(connfd)
                    self.fdmap[connfd.fileno()] = connfd
                else:
                    self.handle(self.fdmap[fd])
                    self.ep.unregister(fd)
                    del self.fdmap[fd]

    # 具体处理请求
    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # request -> {'method':'GET','info':'/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or \
                    request['info'][-5:] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass
        # 将数据发送给HTTPserver
        response = json.dumps(response)
        connfd.send(response.encode())
        connfd.close()

    # 网页处理函数
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR+'/index.html'
        else:
            filename = STATIC_DIR+info

        try:
            fd = open(filename)
        except:
            f = open(STATIC_DIR+'/404.html')
            return {'status':'404','data':f.read()}
        else:
            return {'status':'200','data':fd.read()}

    # 处理数据
    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
        return {'status':'404','data':'Sorry...'}

if __name__ == '__main__':
    app = Application()
    app.start()







