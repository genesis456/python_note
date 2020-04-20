"""
day11作业(重点（面试类题）)

请用面向对象思想，描述以下场景：
    张无忌　教　赵敏　九阳神功
    赵敏　教　张无忌　化妆
    张无忌　上班　挣了　10000
    赵敏　上班　挣了　6000
    体会：对象区分是数据的不同。
"""
"""
张无忌和赵敏是名字（数据）的不同，只需做一个类．　而九阳神功和化妆只是它们类中的行为不同
上班挣了是行为
"""

class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    def teach(self,other,kill):
        """
        教
        """
        print(self.name,"教",other.name,kill)

    def work(self,money):
        """
        上班挣了
        """
        print(self.name,"上班挣了",money)


re = Person("张无忌")
zm = Person("赵敏")
re.teach(zm,"九阳神功")
zm.teach(re,"化妆")
# re.work(10000)
# zm.work(6000)












