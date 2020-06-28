"""
测试用例
"""



# 计算
def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1

# IO
def io():
    write1()
    read1()

def write1():
    f = open('test','w')
    for i in range(200000):
        f.write("hello world\n")
    f.close()

def read1():
    f = open('test')
    lines = f.readlines()
    f.close()
