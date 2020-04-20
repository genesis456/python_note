"""
with.py
使用with 打开文件
"""

# 生成文件对象f
with open('test') as f:
    data = f.read()
    print(data)

# with语句块结束 f 自动销毁
