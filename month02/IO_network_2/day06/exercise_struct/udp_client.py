"""

udp客户端
"""


# from socket import *
# from struct import *
# #先定义数据格式
# st = Struct('i32sif')
# #创建套接字
# sockfs = socket(AF_INET,SOCK_DGRAM)
# #服务端地址
# ADDR = ('127.0.0.1',8484)
# #循环s收发消息
# while True:
#     id = int(input("ID:"))
#     if not id:
#         break
#     name = input("Name:").encode()
#     age = int(input("age:"))
#     socre = float(input("socre:"))
#
# #将数据打包发送
#     data = st.pack(id,name,age,socre)
#     sockfs.sendto(data,ADDR)
#     msg,addr = sockfs.recvfrom(10)
#     print("from server:",msg.decode())
# sockfs.close()

from socket import *
import struct

sockfd = socket(AF_INET,SOCK_DGRAM)
ADDR = ('127.0.0.1',8484)

st = struct.Struct('i16sif')

def udp_send(sockfd,*args):
    data = st.pack(args[0],args[1].encode(),args[2],args[3])
    sockfd.sendto(data,args[-1])

while True:
    id = input("输入id:")
    if not id:
        break
    id = int(id)
    name = input("输入名字：")
    age = int(input("输入年龄:"))
    score = float(input("输入成绩："))

    udp_send(sockfd,id,name,age,score,ADDR)
sockfd.close()