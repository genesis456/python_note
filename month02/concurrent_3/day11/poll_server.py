"""
poll_server　完成ｔｃｐ并发服务
重点代码

【1】 创建套接字
【2】 将套接字register
【3】 创建查找字典，并维护
【4】 循环监控IO发生
【5】 处理发生的IO
"""

from socket import *
from select import *

#创建监听套接字
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',5454))
s.listen(5)

#创建poll对象
p = poll()

#建立查找字典，通过IO的fileno(描述符)查找io对象
#且始终与register 的IO保持一致
fdmap = {s.fileno() : s}

#关注 s
p.register(s,POLLIN|POLLERR)

#循环监控ＩＯ发生
while True:
    event = p.poll() #阻塞等待IO发生
    #循环遍历查看哪个IO准备就绪,进行处理
    for fd,event in event:   #event是一个［（描述符，事件类型）］
        #区分哪个IO就绪
        if fd == s.fileno():
            c,addr = fdmap[fd].accept()
            print("Connect from ",addr)
            #关注客户端连接套接字
            p.register(c,POLLIN|POLLHUP)
            fdmap[c.fileno()] = c  # 维护字典
        elif event & POLLIN:  #判断是否为POLLIN（读IO事件）就绪，是返回Ｔrue
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd) #取消监控
                fdmap[fd].close()
                del fdmap[fd]  # 从字典删除
                continue
            print(data)
            p.register(fdmap[fd],POLLOUT)
        elif event & POLLOUT:  #判断是否为POLLOUT（写IO事件）就绪
            fdmap[fd].send(b'OK')
            p.register(fdmap[fd], POLLIN)















