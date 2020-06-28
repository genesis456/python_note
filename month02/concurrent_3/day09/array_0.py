"""
作者：周乐
日期：2020/3/18
进程通信3：
    共享内存方法２
    array.py
    共享内存存放一组数据
"""

from multiprocessing import Process,Array

#创建共享内存
# shm = Array('i',[1,2,3,4])  #列表中数据只能有一种类型（i整型）
#或
# shm = Array('i',5)  #若里面放的不是列表（表示初始开辟５个整型空间[0,0,0,0,0]）
#或
shm = Array('c',b'hello')   #字节串


def fun():
    #array 创建共享内存对象可迭代
    for i in shm:
        print(i)
    shm[1] = 1000 #修改共享内存

p = Process(target=fun)
p.start()
p.join()
for i in shm:  #在一个进程修改，另一个进程也能拿到
    print(i)

print(shm.value) #打印字节串









