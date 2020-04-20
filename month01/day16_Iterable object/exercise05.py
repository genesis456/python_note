"""
    迭代器练习：定义MyRange类，实现下列功能
    for item in range(10):
        print(item)
"""

class MyRange:   #1先定义__iter__
    def __init__(self,value):
        self.__value = value

    def __iter__(self):
        return MyRangeAtor(self.__value)  #2根据__iter__创建MyRangeAtor迭代器

class MyRangeAtor:
    def __init__(self,stop_value):   #3将数据传进来，获取每一个数据
        self.__stop_value = stop_value
        self.__number = 0
    def __next__(self):
        if self.__number == self.__stop_value:
            raise StopIteration
        temp = self.__number
        self.__number += 1
        return temp

#__next__；执行一次，存一次，（就算数据再大也不会很占内存，打印一次之后就会被丢弃，打印下一个）
for item in MyRange(10):  #将MyRange(10)传上去
    print(item)