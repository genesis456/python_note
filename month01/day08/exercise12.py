

# 练习:定义函数，数值相加的函数.:

#如果传入的参数过多，可以使用*args元组
def adds(*args):
    result = 0
    for item in args:   #将传入的所有参数都拿出来
        result += item
    return result     #返回想要的相加和


print(adds(1,23,5,845,21,5,6))
print(adds(1,23,5,6))


# 作业:调用fun07。
def fun07(a, b, *args, c, d, **kwargs):
    print(a)
    print(a,b)
    print(args)
    print(c,d)
    print(kwargs)

fun07(1,2,3,4,c=5,d=6,e=4,u=2)  #星号元组后面一定要跟命名关键字

#位置实参无限＋关键字实参无限
def fun01(*args,**kwargs):
    print(args)
    print(kwargs)
fun01(1,2,3,4,a=6,b=8)

