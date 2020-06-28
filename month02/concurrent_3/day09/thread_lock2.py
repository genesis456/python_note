"""
互斥锁演示２
"""

import threading
import time

g_num = 0

def test1(num):
    global g_num
    #上锁，如果之前没有被上锁，那么此时  上锁成功
    #如果上锁之前  已经被上锁了，那么此时会阻塞在此，直到这个锁被解开位置
    mutex.acquire()

    for i in range(num):
        g_num += 1
    #解锁
    mutex.release()
    print("---test1 g_num=%d---" %g_num)


def test2(num):
    global g_num
    mutex.acquire()

    for i in range(num):
        g_num += 1
    mutex.release()
    print("---test2 g_num=%d---" %g_num)

#创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()

def main():
    t1 = threading.Thread(target=test1,args=(1000000,))
    t2 = threading.Thread(target=test2,args=(1000000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(2)
    print("---main g_num=%d---"% g_num)

if __name__ == '__main__':
    main()

#用互斥锁解决了资源争夺的问题，一个先执行，一个后