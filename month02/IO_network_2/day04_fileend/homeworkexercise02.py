"""
编写一个程序，向一个文件写入如下内容

          1. 2019-1-1  18:18:18
          2. 2019-1-1  18:18:20


       每隔2秒写入一次，每条占一行。
       ctrl-c/红点 结束程序，下次启动后序号要跟之前的连续
       需要可以在编辑器中实时看到文件写入情况
"""
###在ＶＳcode进行效果明显
import time

f = open('log.txt','ab+')  #以二进制读写模式打开并可以追加

# 文件偏移量定位到开头
f.seek(0)
n = 0
# 获取有多少行
for line in f:    #想断开之后再次重新连上，先要遍历之前的有多少行了．然后在下一行继续进行
    n += 1

# f.seek(-29,2) # 移动到最后一行开头
# data = f.readline().decode()
# n = int(data.split('.')[0]) # 获取行号

while True:
    n += 1
    time.sleep(2)  #sleep(t)  推迟执行的秒数
    s = "%d. %s\n"%(n,time.ctime())   #获取当前时间戳，转换为字符串时间的秒数。
    f.write(s.encode())   #将字符串以二进制写入
    f.flush()   # 随时查看（刷新缓存区）
    #print(f.fileno())  #查看文件标识符用的

