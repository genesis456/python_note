#udp 客户端流程
from socket import *

sockfs = socket(AF_INET,SOCK_DGRAM)
#服务端地址
ADDR = ('127.0.0.1',8880)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#循环收发消息
while True:
    data = input("word>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR) #将消息字节串转为字符串发送给服务端
    msg,addr = sockfd.recvfrom(1024) #接收消息
    print("From server:",msg.decode())

#关闭套接字
sockfd.close()