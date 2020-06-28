"""
thread_lock.py
线程锁演示（处理资源争夺方法2）
"""
from threading import Thread,Lock

a = b = 0
lock = Lock()  #定义锁

def value():
    while True:
        lock.acquire()  #上锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = Thread(target=value)
t.start()
while True:
    with lock:   #上锁
        a += 1
        b += 1

t.join()