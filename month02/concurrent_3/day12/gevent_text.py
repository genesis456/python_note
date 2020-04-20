"""
gevent 协程模块
"""

import gevent

#协程函数
def foo(a,b):
    print("Runnung foo...",a,b)
    gevent.sleep(2)
    print("Foo again..")

def bar():
    print("Runnung bar...")
    gevent.sleep(3)
    print("Bar again..")

#生成协程对象
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)
# gevent.sleep(5)  #协程自动运行的触发条件(阻塞)

gevent.joinall([f,b])  #阻塞等待f,b两个协程执行完毕

#缺陷：只能使用该模块的阻塞，不能通用．解决办法：monkey脚本．　见gevent_monkey.py
