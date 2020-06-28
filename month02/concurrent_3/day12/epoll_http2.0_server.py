"""
httpserver  v2.0
env:python3.6
io多路复用　和　http训练　
"""

from socket import *
from select import *

#具体功能实现
class HTTPServer:
    def __init__(self,host='0.0.0.0',port=5454,dir=None):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host,port)
        #创建epoll对象
        self.ep = epoll()
        #创建字典地图
        self.fdmap = {}

        #实例化对象直接创建套接字
        self.create_socket()
        self.bind()

    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    #绑定地址
    def bind(self):
        self.sockfd.bind(self.address)


    #启动服务
    def server_forever(self):
        self.sockfd.listen(3)
        print("Listen the port %d"%self.port)
        #Io多路复用接收客户端请求
        self.fdmap[self.sockfd.fileno()] = self.sockfd
        self.ep.register(self.sockfd,EPOLLIN|EPOLLERR)
        while True:
            events = self.ep.poll()
            for fd,event in events:
                if fd == self.sockfd.fileno():
                    c,addr = self.fdmap[fd].accept()
                    # print("Connect from",addr)
                    self.ep.register(c,EPOLLIN|EPOLLET)
                    self.fdmap[c.fileno()] = c

                else:
                    self.handle(fd,event)
    # 处理请求
    def handle(self,fd,event):

        if event & EPOLLIN:
            # 接收Http请求
            request = self.fdmap[fd].recv(4096).decode()
            # 客户端断开
            if not request:
                self.ep.unregister(fd)
                self.fdmap[fd].close()
                del self.fdmap[fd]
                return


            # 提取请求内容
            request_line = request.splitlines()[0]  # 将字节串按行分割(拿出请求行)
            info = request_line.split(' ')[1]  # 获取请求内容 /
            print(self.fdmap[fd].getpeername(), ':', info)  # 获取客户端地址

            # 根据请求内容进行数据整理
            # 分为两类　　1．请求网页　　2．其他
            if info == '/' or info[-5:] == '.html':  # 请求网页
                self.st =self.get_html(info)# 处理网页
            else:
                self.st = self.get_data() # 其他数据

            self.ep.unregister(fd)
            self.ep.register(self.fdmap[fd], EPOLLOUT)

        elif event & EPOLLOUT:
            self.fdmap[fd].send(self.st.encode())
            self.ep.unregister(fd)
            self.ep.register(self.fdmap[fd], POLLIN)

    # 处理网页
    def get_html(self,info):
        if info == '/':
            # 请求主页
            filename = self.dir + '/index.html'
        else:
            filename = self.dir + info
        try:
            fd = open(filename)
        except Exception:
            # 网页不存在
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry...</h1>'

        else:
            # 网页存在
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Type:text/html\r\n'
            response += '\r\n'
            response += fd.read()

        finally:
            # 将响应发送给浏览器
            return response

    # 其他数据
    def get_data(self):
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type:text/html\r\n'
        response += '\r\n'
        response += '<h1>Waiting for httpserver 3.0</h1>'
        return response


#用户使用HTTPServer
if __name__ == "__main__":
    """
    通过　HTTPServer类快速搭建服务，展示自己的网页
    """
    #用户决定的参数
    HOST = '0.0.0.0'
    PORT = 5454
    DIR = './static'  #网页存储位置

    httpd = HTTPServer(HOST,PORT,DIR)  #实例化对象
    httpd.server_forever()  #启动服务