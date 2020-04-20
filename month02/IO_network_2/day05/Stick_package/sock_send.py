from socket import *
from time import sleep

# 创建tcp套接字(与服务端相同类型的套接字)
sockfd = socket()  # 默认参数-->tcp套接字

# 连接服务端程序
server_addr = ('127.0.0.1',8886)
sockfd.connect(server_addr)

# while True:
#     sleep(0.3)   #0.3秒发送一次
#     sockfd.send(b"hello")

#控制速度
for i in range(10):
    sockfd.send(b"hello#") #或加＃人为边界