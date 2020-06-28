"""
dict 服务端
功能：业务逻辑处理
模型：多进程tcp并发
"""

from socket import *
from multiprocessing import Process
import signal,sys
from mysql_ import *
from time import sleep


#全局变量
HOST = '0.0.0.0'
PORT = 5450
ADDR = (HOST,PORT)

#建立数据库对象
db = Database()  #传入需要的数据库（其他可以默认）



#查询单词
def do_query(c,data):
    tmp = data.split(' ')
    name = tmp[1]
    word = tmp[2]

    #插入历史记录
    db.insert_hist(name,word)

    #没找到返回None  找到返回单词解释
    mean = db.query(word)
    if mean:
        msg = "%s : %s" % (word, mean)

    else:
        msg = "没有找到该单词"
    c.send(msg.encode())

#获取历史记录发送给客户端
def do_hist(c,data):
    name = data.split(' ')[1]
    hist = db.get_hist(name)
    print("hist")
    if not hist:
        c.send(b'Fail')
        return
    c.send(b'OK')
    for i in hist:
        # i -->(name,word,time)
        msg = "%s  %-16s %s" % i  #左对齐，占16个字符
        sleep(0.1)
        c.send(msg.encode())
    sleep(0.1)
    c.send(b'##')


# 服务端注册处理
def do_register(c, data):
    tmp = data.split(' ')  # ('R name passwd')
    name = tmp[1]
    passwd = tmp[2]
    if name == '' or passwd == '':
        c.send(b'Fail')
        return  # 如果用户名或密码为空将退出注册

    # 返回True表示注册成功，False表示失败
    if db.register(name, passwd):
        c.send(b'OK')

    else:
        c.send(b'Fail')


#登录
def do_login(c,data):
    tmp = data.split(' ')  # ('L name passwd')
    name = tmp[1]
    passwd = tmp[2]
    if db.login(name,passwd):
            c.send(b'OK')

    else:
        c.send("登录失败".encode())


def handle(c):
    # 循环接收请求
    while True:
        data = c.recv(1024).decode()

        if not data or data[0] == 'E':
            sys.exit()  # 对应的子进程退出
        elif data[0] == 'R':  #注册
            do_register(c, data)
        elif data[0] == 'L':  #登录
            do_login(c, data)
        elif data[0] == 'Q':  #查单词
            do_query(c, data)
        elif data[0] == 'H':
            do_hist(c,data)



#搭建网络
def main():
    #创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #处理僵尸进程
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)


    #循环等待客户端连接
    print("Listen the port 5450")
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt:  #自行强制终止
            s.close()
            db.close()
            sys.exit("服务端退出")
        except Exception as e:
            print(e)
            continue


        #为客户端创建子进程
        p = Process(target=handle,args=(c,))
        p.daemon = True  #父进程退出子进程也随之退出
        p.start()










if __name__ == '__main__':
    main()