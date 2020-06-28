"""
udp服务端
"""


# from socket import *
# from struct import *
# #和客户端一样的格式
# at = Struct('i32sif')
# sockfd = socket(AF_INET,SOCK_DGRAM)
# ADDR = ('0.0.0.0',8484)
# sockfd.bind(ADDR)
#
# #打开文件
# f = open('student.txt','a')
#
# while True:
#
#     data,addr = sockfd.recvfrom(1024)
#     # 将信息转换位元组数据 (1,b'lily',13,89.5)
#     data = at.unpack(data)
#
#     #写入文件(-10表示左对齐10个宽度)
#     info = "%d  %-10s   %d  %.1f\n"%data
#     sockfd.sendto(b'Thank',addr)
#     f.write(info)
#     f.flush()
# f.close()
# sockfd.close()


from socket import *
import struct
s =socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8484))
sct = struct.Struct('i16sif')

def unpack1(data):

    w = sct.unpack(data)
    info = "%d  %-10s   %d  %.1f\n" % w
    with open('hello.txt','a') as f:
        f.write(info)
        f.flush()
        f.close()

while True:
    data,addr = s.recvfrom(4096)
    if not data:
        break
    unpack1(data)

s.close()