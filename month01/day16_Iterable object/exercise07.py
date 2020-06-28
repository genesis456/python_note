"""
作者：周乐
日期：03/12/2019
生成器练习：
# 练习1:从列表[4,5,566,7,8,10]中选出所有偶数
# -- 结果存入另外一个列表中
# -- 使用生成器实现
"""
# -- 结果存入另外一个列表中
list01 = [4,5,566,7,8,10]
def get_even01():
    result = []
    for item in list01:
        if item % 2 == 0:
            result.append(item)
    return result

re = get_even01()
for item in re:
    print(item)
                                #两者的区别是：第一个调用方法是就会直接执行里面的for循环
                                #而后者利用生成器实现，在调用方法时不会执行里面的程序
                                #而是在生成一个迭代器对象（生成器），实际方法中的程序都是在
                                #迭代器对象的＿＿next＿＿中．所以执行下一步时（for item in g01:）
                                #才跳进方法中的

#以后做的时候，只要方法中要返回多个结果就可以用生成器 yield　完成
#和上面最大区别是　　不占内存，只拿需要的数据（上面是将新的数据又放了一个列表，占内存）


# -- 使用生成器实现
def get_even02():
    for item in list01:
        if item % 2 == 0:
            yield item

g01 = get_even02()
for item in g01:
    print(item)
