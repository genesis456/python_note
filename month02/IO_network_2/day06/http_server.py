"""
http_server   v1.0
基本要求：　　1．获取来自浏览器的请求
            2．判断如果请求内容是／将index.html返回给客户
            3. 如果是，则将 index.html 发送给浏览器
            如果不是，则告知浏览器 sorry
            4. 注意组织http响应格式， 判断 200 or 404
"""

from socket import *
#客户端（浏览器）处理
def request(connfd):

    # 直接获取HTTP请求
    data = connfd.recv(4096)
    if not data:
        return

    # 获取请求将请求内容提取出来
    # print(data)先打印接收到的内容，看怎么拿
    request_line = data.decode().split('\n')[0]  #将收到请求内容转为字符串按＼n换行分割取第一个GET / HTTP/1.1
    # print(request_line)
    info = request_line.split(" ")[1]  #将GET / HTTP/1.1再次以空格分割，取第二个

    #判断是 / 则返回index.html  不是则返回404
    if info == '/':
        with open('index.html') as f:    #默认为r读方式打开
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response += f.read()

    else:
       response = "HTTP/1.1 404 Not Found\r\n"
       response += "Content-Type:text/html\r\n"
       response += "\r\n"
       response += "<h1>Sorry....</h1>"

    connfd.send(response.encode())

#搭建tcp网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('127.0.0.1',8484))
sockfd.listen(5)
while True:
    #等待客户端连接
    connfd,addr = sockfd.accept()
    print("Connect from", addr)
    request(connfd)  #具体处理客户端请求