'''进程池'''

from multiprocessing import Pool
import time

#事件函数
def fun01(msg):
    time.sleep(2)
    print(msg)

# 1.创建进程池对象
pool = Pool()
# 2.讲事件加入到进程池队列执行
for i in range(10): #添加10个事件
    msg = '我是第%d个消息'%i
    pool.apply_async(fun01,args=(msg,))

# 3.关闭进程池
pool.close()
# 4.回收进程池中的进程
pool.join()