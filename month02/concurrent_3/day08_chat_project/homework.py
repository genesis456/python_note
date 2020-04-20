"""
作业：1. 聊天室代码 周末梳理思路
     2. process 使用
     3. 使用两个子进程（process）分别复制
     一个文件的上下半部分，将内容各自复制到
     一个新的文件中。

"""

from multiprocessing import Process
import os

filename = './timg.jpeg'
size = os.path.getsize(filename) #获取图片大小

#复制上半部分
def top():
    fr = open(filename,'rb')
    fw = open('top.jpg','wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

#复制下半部分
def bot():
    fr = open(filename,'rb')
    fw = open('bop.jpg','wb')
    fr.seek(size//2)
    fw.write(fr.read())
    fr.close()
    fw.close()

p1 = Process(target=top)
p2 = Process(target=bot)
p1.start()
p2.start()
p1.join()
p2.join()