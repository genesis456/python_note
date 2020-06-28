"""
file_write.py
文件写操作
"""

# 打开文件
# f = open('a.py','a')
f = open('a.py','w') #若文件不存在就自动新建

# 写操作　　　　　都要人为加\n换行
# f.write("hello python\n")
# f.write("out,ccc\n")

# 将列表中每一项分别写入文件内(一般采用writelines())
l = ['hello world\n','hello kitty\n']
f.writelines(l)


# f.close()
