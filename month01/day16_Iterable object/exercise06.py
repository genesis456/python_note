"""
迭代器 --> yield
   练习: 将迭代器版本的图形管理器改为yield实现.
        exercise03.py -->exercise06.py
"""

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

        # number = 0
        # while number < len(self.__graphic):
        #     yield self.__graphic[number]
        #     number += 1
        for item in self.__graphic:  #更加简便
            yield item

mess = GraphicManager()
mess.add_graphic(Graphic())
mess.add_graphic(Graphic())
mess.add_graphic(Graphic())

# for item in mess:
#     print(item)

iterator = mess.__iter__()   #执行这的时候，不会执行上面__iter__，
                            # 而是继续往下走（因为上面那个表面是__iter__，实际用的是＿＿next__）
                            #
while True:
    try:
        item = iterator.__next__()   #调到上面__iter__中
        print(item)
    except StopIteration:
        break