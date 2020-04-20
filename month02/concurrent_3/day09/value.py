"""
作者：周乐
日期：2020/3/18
进程通信3：
    共享内存方法1
    value.py 开辟单一个共享内存空间
    注意：共享内存只能有一个值
"""
from multiprocessing import Process,Value
import time
import random

#创建共享内存
money = Value('i',5000)   #i表示整型，一定要写上后面参数的类型

#操作共享内存
def man():
    for i in range(30):
        time.sleep(0.2)
        money.value += random.randint(1,1000)

def girl():
    for i in range(30):
        time.sleep(0.15)
        money.value -= random.randint(100,800)


p1 = Process(target=man)
p2 = Process(target=girl)
p1.start()
p2.start()
p1.join()
p2.join()

#获取共享内存
print("一个月余额：",money.value)

