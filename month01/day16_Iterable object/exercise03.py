# 迭代器练习：图形管理器记录多个图形
#      迭代图形管理器对象

class Graphic:
    pass


class GraphicManager:
    """
        图形管理器，可迭代对象(参与for)
    """
    def __init__(self):
        self.__graphic = []

    def add_graphic(self,graphics):
        self.__graphic.append(graphics)

    def __iter__(self):
        return GraphicAtor(self.__graphic)   # 创建一个迭代器对象,并调用需要迭代的数据(也就是列表)

class GraphicAtor:
    """
    图形迭代器（获取下一个数据）
    """

    def __init__(self,gerta):   #传进来的是列表
        self.__gerta = gerta
        self.__number = 0

    def __next__(self):  #next做的是遍历，如果超出范围就报错
        if self.__number > len(self.__gerta)-1:  #如果大于最大索引就报错
            raise StopIteration

        # 返回下一个数据
        temp = self.__gerta[self.__number]
        self.__number += 1
        return temp

mess = GraphicManager()
mess.add_graphic(Graphic())
mess.add_graphic(Graphic())
mess.add_graphic(Graphic())

for item in mess:   #单独写for，mess会报错．（要一起写上for的原理__iter__）
    print(item)

iterator = mess.__iter__()   #iterator是__iter__中的返回值
while True:
    try:
        item = iterator.__next__()   #因为__next__要将返回的结果给item（所以要在iterator中创建__next__的方法）
        print(item)
    except StopIteration:
        break





