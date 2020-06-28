"""
广播发送
1.创建udp套接字
2.设置可以发送广播
3.循环向广播地址发送

"""

from socket import *
from time import sleep
#广播地址
dest = ('0.0.0.0',8484)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
data = """
        **********
        湖南　8.2
        温度：35
        状态：很惨
        **********
"""
while True:
    sleep(2)
    s.sendto(data.encode(),dest)