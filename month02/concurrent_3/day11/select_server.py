"""
select  tcp服务
重点代码

思路分析：
1. 将关注的ＩＯ放入监控列表
2. 当ＩＯ就绪时通知ｓｅｌｅｃｔ返回
3. 遍历返回值列表，处理就绪的ＩＯ

"""

from socket import *
from select import select

#创建监听套接字，作为关注的io
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',5454))
s.listen(5)

#设置关注的IO列表
rlist = [s]  #s 用于等待处理连接
wlist = []
xlist = []

#循环ＩＯ监控
while True:
    rs,ws,xs = select(rlist,wlist,xlist)

    # 遍历返回值列表，判断哪个ＩＯ就绪
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)  #若有客户端连接上就增加一个新关注的ＩＯ
        else:   #[c]
            #表明有客户端发送消息
            data = r.recv(1024).decode()
            if not data:
                rlist.remove(r) #取消对客户端关注
                r.close()
                continue  #跳过本次（因为还有其他客户端的套接字）
            print(data)
            # r.send(b'OK')
            wlist.append(r) #给我发消息的客户端

    for w in ws:
        w.send(b'OK')
        wlist.remove(w) #发完消息就移除（不然会一直在此循环）
    for x in xs:
        pass
