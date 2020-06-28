"""
udp_client.py   udp客户端流程
重点代码
"""

from socket import *

#服务端地址
ADDR = ('127.0.0.1',8484)

#创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

#循环收发消息
while True:
    data = input("Msg>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR) #将消息字节串转为字符串发送给服务端
    msg,addr = sockfd.recvfrom(10) #接收消息
    print("From server:",msg.decode())

#关闭套接字
sockfd.close()