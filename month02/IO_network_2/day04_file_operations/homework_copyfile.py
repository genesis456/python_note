"""
练习1: 编写一个程序,从终端输入一个单词,可以打印出单词及其解释,如果没有这个单词则打印 "没有该单词"
exercise01.py

练习2： 将一个文件拷贝一份，文件可能是文本文件也可能是二进制文件

e.g.  'test.jpg' ---> 'test-bak.jpg'

homeworkday04.py

作业 ： 1. 熟悉文件的基本读写操作，open打开方式特征

       2. 编写一个程序，向一个文件写入如下内容

          1. 2019-1-1  18:18:18
          2. 2019-1-1  18:18:20


       每隔2秒写入一次，每条占一行。
       ctrl-c/红点 结束程序，下次启动后序号要跟之前的连续
       需要可以在编辑器中实时看到文件写入情况
"""
"""
将一个文件拷贝一份，
文件可能是文本文件也可能是二进制文件
"""

#输入文件名
filename = input("file:")
try:
    st = open(filename,'rb')  #不知道是文本文件还是二进制文件，可以都通过二进制打开

except FileNotFoundError as e:  #若文件不存在就执行
    print(e)
else:
    sw = open("file.jpg",'wb')#二进制写入打开(要加上复制的后缀，不然就变成普通文本文件)
    # 循环读取文件直到最后
    while True:
        data = st.read(1024) #每次读取1024个字节,
        if not data:  #  文件结束
            break
        sw.write(data)  #将接收到的文件写入新文件

    st.close()   #关闭所有文件
    sw.close()


