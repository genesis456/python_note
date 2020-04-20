"""
multiprocessing  模块创建进程
1、编写进程函数
2、生产进程对象
3、启动进程
4、回收进程
"""

import multiprocessing as mp
from time import sleep

a =1

#进程函数
def fun():
    print("开始一个进程")
    sleep(2)
    global a
    print("a:", a)
    a = 1000
    print("子进程结束")

# 创建进程对象
p = mp.Process(target = fun) #p可以代表一个进程
p.start() #启动进程

#父进程事件
sleep(3)
print("父进程干的事")

p.join()  #回收进程
print("a:",a)

#等同于fork(原理和fork一样)
"""
pid = os.fork()
if pid ==0:
    fun()
    os._exit()
else:
    os.wait()
"""