"""
HTTPServer 部分的主程序

获取http请求
解析http请求
从WebFrame接收反馈数据
将数据组织为Response格式发送给客户端

"""

from socket import *
import sys
from threading import Thread
from config import *
import re,json

#服务器地址
ADDR = (HOST,PORT)

#和 web frame 通信的函数
def connect_frame(env):
    s = socket()
    try:
        s.connect((frame_ip,frame_port))
    except Exception as e:
        print(e)
        return
    # 将字典转换为json
    data = json.dumps(env)
    # 将解析后的请求发送给webframe
    s.send(data.encode())
    # 接收来自Webframe数据
    data = s.recv(1024 * 1024 * 10).decode()
    return json.loads(data)  # 收到的json数据json.loads(data)转字典


#将httpserver 基本功能封装为类
class HTTPServer:
    def __init__(self):
        self.address = ADDR
        self.create_socket() #和浏览器交互的套接字
        self.bind()

    #创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)

    # #创建和webframe交互的套接字
    # def connect_socket(self):
    #     self.connect_sockfd = socket()
    #     frame_addr = (frame_ip,frame_port)
    #     try:
    #         self.connect_sockfd.connect(frame_addr)
    #     except Exception as e:
    #         print(e)
    #         sys.exit()

    #绑定地址
    def bind(self):
        self.sockfd.bind(self.address)
        self.ip = self.address[0]
        self.port = self.address[1]

    #启动服务
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"% self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            #connfd不能变成self.connfd属性变量，属性变量是类中共用的，第二个连接会修改属性变量值
            print("Connect from ",addr)
            client = Thread(target=self.handle,args=(connfd,))
            client.setDaemon(True)
            client.start()

    #具体处理客户端请求任务
    def handle(self,connfd):
        #获取HTTP请求
        request = connfd.recv(4096).decode()
        pattern = r'(?P<method>[A-Z]+)\s+(?P<info>/\S*)'  #用正则来获取 Get / (捕获组返回字典形式)
        try:
            env = re.match(pattern,request).groupdict()
            #groupdict()返回捕获组名与内容组合成字典形式

        except:
            #　客户端断开
            connfd.close()
            return
        else:
            data = connect_frame(env)
            self.response(connfd,data)


    #给浏览器发送数据
    def response(self,connfd,data):
        # data => {'status':'200','data':'xx'}
        if data['status'] == '200':
            responseHeaders = "HTTP/1.1 200 OK\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']


        elif data['status'] == '404':
            responseHeaders = "HTTP/1.1 404 Not Found\r\n"
            responseHeaders += "Content-Type:text/html\r\n"
            responseHeaders += "\r\n"
            responseBody = data['data']

        #给浏览器发送数据
        response_data = responseHeaders + responseBody
        connfd.send(response_data.encode())



httpd = HTTPServer()
httpd.serve_forever()






