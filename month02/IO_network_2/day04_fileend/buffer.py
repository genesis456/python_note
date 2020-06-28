"""
buffer.py
缓冲区刷新测试
"""

f = open('a.py','w',1) # 1表示进行行缓冲区刷新
# f = open('b.py','w')

while True:
    data = input(">>")
    if not data:
        break
    f.write(data + '\n')   #每换一次行，就刷新缓冲区（将缓冲区内容写入磁盘）
    # f.flush()  # 刷新缓冲区

f.close()