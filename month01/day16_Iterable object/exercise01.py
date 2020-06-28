"""
作者：周乐
日期：29/11/2019
 可迭代对象练习1：使用迭代器原理，遍历元组.
 ("铁扇公主","铁锤公主",“扳手王子”)
"""
tuple01 = ("铁扇公主","铁锤公主","扳手王子")

iterator = tuple01.__iter__()  #获取可迭代对象
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
