"""
递归练习： 函数，有一个参数传入整数，返回该整数的阶乘
5！ == 5*4*3*2*1

求一个数的阶乘  n!

多熟悉递归应用
"""

def fun(n):
    result = 1
    for i in range(1,n + 1):
        result *= i
    return  result



def recursion(n):
    if n <= 1:
        return 1
    return n * recursion(n - 1)

print(recursion(5))














