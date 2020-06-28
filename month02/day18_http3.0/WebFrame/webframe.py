"""
webframe.py　　模拟后端应用工作流程
从httpserver接收具体请求
根据请求进行逻辑处理和数据处理
将需要的数据反馈给httpserver
"""


from socket import *
import json
from settings import *
from select import *
from urls import *

#应用类，处理某一方面的请求
class Application:
    def __init__(self):
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,DEBUG)
        self.sockfd.bind((frame_ip,frame_port))

    #启动服务
    def start(self):
        self.sockfd.listen(5)
        print("Start app listen %s"% frame_port)
        self.rlist.append(self.sockfd)
        #select 监控请求
        while True:
            rs,ws,xs = select(self.rlist,
                              self.wlist,
                              self.xlist)
            for r in rs:
                if r is self.sockfd:
                    connfd,addr = r.accept()
                    self.rlist.append(connfd)
                else:
                    self.handle(r)
                    self.rlist.remove(r)

    #处理具体的httpserver 请求
    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        request = json.loads(request)
        # print(request)
        # d = {'status':'200','data':'xxxx'}
        # connfd.send(json.dumps(d).encode())

        #request=> {'method':'GET','info':'/'}
        if request['method'] == 'GET':
            if request['info'] == '/' or \
                request['info'][-5] == '.html':
                response = self.get_html(request['info'])
            else:
                response = self.get_data(request['info'])
        elif request['method'] == 'POST':
            pass

        #将数据发送给httpserver
        #response = json.dumps(response
        resp = json.dumps(response)
        connfd.send(resp.encode())
        connfd.close()

    #处理网页
    def get_html(self,info):
        if info == '/':
            filename = STATIC_DIR + "/index.html"
        else:
            filename = STATIC_DIR + info
        try:
            fd = open(filename)
        except:
            f = open(STATIC_DIR + "/404.html")
            return {'status':'404','data':f.read()}
        else:
            return {'status':'200','data':fd.read()}


    #处理数据
    def get_data(self,info):
        for url,func in urls:
            if url == info:
                return {'status':'200','data':func()}
        return {'status':'404','data':"Sorry..."}


app = Application()
app.start()  #启动应用服务


#
# 1. 并发使用场景
#
#    python
#    * 需要使用多核的计算密集型并发 就用进程
#    * IO并发优先线程或者IO多路服用
#      如果请求需要长期占有服务用线程
#
#    其他语言
#    * 计算密集型并发优先线程
#    * IO并发多路服用
#
#    c, c++
#    * 功能独立,多进程
#    * 关联性强的功能多线程
#    * IO 并发多路服用
#
# 2. 数结构研究方向
#
#    链表 : 单循环链表  双向循环链表
#    二叉树 : 平衡二叉树, B树, 红黑树
#    图 : 了解
#    算法 : 快速排序, 哈希存储, 归并,分治递归,动态规划
#
# 3. 进程间通信方法 :  消息队列 套接字 (rabbitmq)
#    io多路服用 : epoll()


