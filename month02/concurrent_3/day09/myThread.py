
"""
mythread.py
练习：给出一个线程实践，完成线程类（主要考察函数的传参）
"""
# from threading import Thread
# from time import sleep,ctime
#
# class MyThread(Thread):
#     def __init__(self,target=None,args=(),kwargs={}):
#         super().__init__()  #此行不许传参
#         self.target = target
#         self.args = args
#         self.kwargs = kwargs
#
#     def run(self):
#         player(*self.args,**self.kwargs)
#
# ######################
#
# def player(sec,song):
#     for i in range(3):
#         print("Playing %s : %s" % (song,ctime()))
#         sleep(sec)
#
# t = MyThread(target=player, args=(3,),
#              kwargs={'song':'凉凉'})
#
# t.start()
# t.join()



from threading import Thread
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target=None,args=(),kwargs={}):
        self.target = target
        self.args = args
        self.kwargs = kwargs

        super().__init__()

    def run(self):
        player(*self.args,**self.kwargs)

def player(second,song):
    for i in range(3):
        print('正在播放 %s:%s'%(song,ctime()))
        sleep(second)

t = MyThread(target=player,args=(3,),
             kwargs={'song':'老鼠爱大米'})
t.start()
t.join()