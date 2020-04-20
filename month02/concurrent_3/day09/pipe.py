"""
作者：周乐
日期：2020/3/18
进程通信１：
    pipe.py  管道通信
    注意：1、multiprocessing 中管道通信只能用于
            有亲缘关系进程中
           2、管道对象在父进程中创建，子进程通过父进程获取
"""

from multiprocessing import Process,Pipe

#创建管道
#默认是双向通道（True），Flase是单向通道
# （一个写，一个读。一个进程中不能将fd1,fd2两个都写一起（容易出现进程争夺出错））
fd1,fd2 = Pipe()

def app1():
    print("启动app 1,请登录")
    print("请求aap2 授权")
    fd1.send("app1 请求登录")  #用fd1进行写入管道
    data = fd1.recv()
    if data:
        print("登录成功：",data)
def app2():
    data = fd2.recv()  #使用fd2阻塞等待读取管道内容
    print(data)
    fd2.send(('Dave','123'))  #可以发送任意python类型

p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()



