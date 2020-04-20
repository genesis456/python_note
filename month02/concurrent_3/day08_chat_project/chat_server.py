"""
服务端
chat room
env:python3.6
socket udp & fork
"""
from socket import *
import os,sys

"""
全局变量：很多封装模块都要用或者有一定得固定含义
"""
#服务器地址
ADDR = ('0.0.0.0',8480)

#存储用户{name:address}
user = {}

#进入聊天室
def do_login(s,name,addr):
    if name in user or '管理员' in name:
        s.sendto("该用户存在".encode(),addr)
        return


    #通知其他人
    msg = '\n欢迎‘%s’进入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    user[name] = addr  #插入字典
    s.sendto(b'OK', addr)



#聊天
def do_chat(s,name,text):
    msg = "\n%s:%s"%(name,text)
    for i in user:
        #刨除其本人
        if i != name:
            s.sendto(msg.encode(),user[i])

#退出
def do_quit(s,name):
    msg = '\n%s 退出聊天室'%name
    for i in user:
        if i != name:  #其他人
            s.sendto(msg.encode(),user[i])
        else:
            s.sendto(b'EXTT',user[i])
    del user[name]  #删除用户



#处理请求
def do_request(s):
    while True:
        data,addr = s.recvfrom(1024)  #收到消息三部分：类型（LCQ），name,内容
        # print(data.decode())
        tmp = data.decode().split(' ')  #拆分请求
        #根据不同得请求类型具体执行不同的事情
        # L 进入   C  聊天   Q 退出
        if tmp[0] == 'L':
            do_login(s,tmp[1],addr)  #执行具体工作

        elif tmp[0] == 'C':
            text = ' '.join(tmp[2:])  #内容可能会出现空格，就先把name后面开始空格拼接成一个整体
            do_chat(s,tmp[1],text)

        elif tmp[0] == 'Q':
            if tmp[1] in user:
                do_quit(s,tmp[1])

#搭建网络
def main():
    #udp服务端
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    if pid ==0:  #子进程处理管理员消息
        while True:
            msg = input("管理员消息:")
            msg = "C 管理员 "+msg
            s.sendto(msg.encode(),ADDR)
            #将管理员消息发给父进程，父进程发送给其他客户端
    else:
        #请求处理函数
        do_request(s)

main()


