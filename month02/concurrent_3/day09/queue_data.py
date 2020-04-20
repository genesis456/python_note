"""
作者：周乐
日期：2020/3/18
进程通信2
    queue_data.py  消息队列演示
    注意：消息队列符合先进先出原则
"""

#双色球
from multiprocessing import Queue,Process

from random import randint

#创建消息队列
q = Queue(5)

def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)  #消息入队
    q.put(randint(1,16))

# end=''在进程中也存在缓冲空间，遇到换行刷新缓冲区，而改成空格，就要等全部执行完才刷新

def request():
    l =[]
    for i in range(6):
        l.append(q.get())  #出队
    l.sort()
    l.append(q.get())
    print(l)


p1 = Process(target=handle)
p2 = Process(target=request)
p1.start()
p2.start()
p1.join()
p2.join()




