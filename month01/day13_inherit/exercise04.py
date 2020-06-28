"""
    定义图形管理器类
        1. 管理所有图形
        2. 提供计算所有图形总面积的方法

    具体图形:
        圆形(pi × r ** 2)
        矩形(长*宽)
        ...

    测试：
        创建1个圆形对象，1个矩形对象，添加到图形管理器中.
        调用图形管理器的计算面积方法，输出结果。

    要求：增加新图形，不修改图形管理器的代码.    (加新图形只需要加类，无需修改)
    体会：面向对象三大特征：
            封装/继承/多态
         面向对象设计原则：
            开闭/单一/倒置

"""

class Graphic_organizer:
    """
    图形管理器类
    """
    # 1. 管理所有图形
    def __init__(self):
        self.__graphics = []   #因为是是管理图形，所以要建立一个列表来存放（设为私有的，只能这个类才能改动）

    def add_graphic(self,graphic):
        if isinstance(graphic,Graph):  #如果传入进来的图形是在Graph类的，就添加
            self.__graphics.append(graphic)
        else:
            raise ValueError()  #否则执行报错

    #2. 提供计算所有图形总面积的方法
    def get_total_area(self):
        # 遍历图形列表，累加每个图形的面积
        total_area = 0
        for item in self.__graphics:
            # 多态：调用父，执行子.
            #调用的是图形
            #执行的是图形里的圆形／矩形
            total_area += item.calculate_area()  #调用一个图形面积item.calculate_area()
            return total_area


class Graph:
    """
    图形类
    """

    def calculate_area (self):  #所有子类的行为必须要和父类的一样，不能改变．

        # 如果子类不重写，则异常.
        raise NotImplementedError()

#-------------------------以上是架构师的框架－－－－－－－－－－

class Roundness(Graph):
    """
    圆形(pi × r ** 2)
    """
    def __init__(self, radius):    #所有子类的行为必须要和父类的一样，不能改变．
        self.radius = radius        #想要参数自己从外面调，而不能向父类要

    def calculate_area(self):
        return 3.14 * self.radius **2

class Rectangle(Graph):
    """
    矩形(长*宽)
    """
    def __init__(self,length,wide):
        self.length = length
        self.wide = wide

    def calculate_area(self):
        return self.length * self.wide

c0 = Roundness(8)
c1 = Rectangle(7,8)
mange = Graphic_organizer()
mange.add_graphic(c0)
mange.add_graphic(c1)
re = mange.get_total_area()
print(re)