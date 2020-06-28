"""
粘包演示(只有tcp才会发生粘包)
处理的方法：
    人为的添加消息边界
    控制发送速度
"""
from socket import *
from time import sleep
#创建tcp套接字
sockfd = socket()

#绑定地址
sockfd.bind(("0.0.0.0",8886))

#设置监听
sockfd.listen(5)

connfd,addr = sockfd.accept()

while True:
    # sleep(1)     #发送和接收的速率不协调，引发生粘包．多个内容被一次接收了
    data = connfd.recv(1024)
    if not data:
        break
    print(data.decode())