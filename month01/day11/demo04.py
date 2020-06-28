"""
    封装设计思想（用面向对象描述）
        需求：老张开车去东北
"""

#老张（可能会变的量，单独作一个类）
class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def go_to(self, str_postion, type):
        """
            去
        :param str_postion: 位置
        :param type: 方式　
        """
        print(self.name, "去", str_postion)
        type.run(str_postion)

#车（可能会变的量，单独作一个类）
class Car:
    def run(self, str_position):
        """
            行驶
        :param str_position: 位置　
        """
        print("汽车行驶到:", str_position)


lz = Person("老张")
car = Car()
# 老张开车去东北
lz.go_to("东北", car)
