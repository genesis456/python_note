"""
seek.py  文件偏移量测试
"""

# 以r,w打开文件偏移量在开头，以a打开文件偏移量在结尾
f = open("a.py",'rb+')
print(f.tell())   #获取文件偏移量的大小

f.write(b"Hello world")

print(f.tell())

# 以开头为基准向后移动5个字符
f.seek(1024,0)  #0表示文件偏移量在开头，移动1024个字节

f.write('你好'.encode())
# data = f.read()
# print(data)

f.close()
