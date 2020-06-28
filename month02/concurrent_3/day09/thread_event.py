
"""
thread_event.py
    event 线程互斥方法演示（处理资源争夺问题方法1）
"""
from threading import Thread,Event

s = None  #用于通信
e = Event()  #事件对象

def cipher():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()   #操作完共享资源


t = Thread(target=cipher)
t.start()
print("说对口令就是自己人")
e.wait()   #阻塞等待，直到操作完共享资源
if s == "天王盖地虎":
    print("宝塔镇河妖")
else:
    print("打死他...")
t.join()
