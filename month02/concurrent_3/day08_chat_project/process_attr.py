'''
进程对象的属性
'''

from multiprocessing import Process
import time

def tm():
    for i in range(3):
        time.sleep(2)
        print(time.ctime())

p = Process(target=tm,name='koko')
#进程名称
# print('Name:',p.name)
# 进程PID
# print('PID:',p.pid) # 没有创建出来的ID为None

# 查看进程是否在生命周期
# print('is alive:',p.is_alive())

p.daemon = True
p.start()

time.sleep(3)
print('hello world')
