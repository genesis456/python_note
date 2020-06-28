"""
套接字属性介绍
"""

from socket import *

# 创建套接字对象
s = socket(AF_INET,SOCK_STREAM)

# 设置端口立即重用(不会出现端口已被使用),一般写在绑定前面
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('127.0.0.1',8881))
s.listen(3)
c,addr = s.accept()

print(s.type)  # 套接字类型
print(s.family) # 地址类型
print(s.getsockname()) # 绑定的地址
print(s.fileno()) # 文件描述符
#连接套接字调用　　结果同accept返回的addr
print(c.getpeername())  # 获取连接端的地址

c.recv(1024)





