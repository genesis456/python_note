"""
使用标准属性,封装变量.(demo03练习)
将exercise02代码优化
"""

class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk
                            # 方法重写，多态　　调用方法名实现不同的功能

    @atk.setter
    def atk(self,value):
        if 10 <= value <= 50:
            self.__atk  = value
        else:
            raise ValueError("超出")

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self,value):
        if 100 <= value <= 200:
            self.__hp  = value
        else:
            raise ValueError("超出")


cs = Enemy("巴基",10,150)
cs.atk = 40
print(cs.atk)
cs.hp = 120
print(cs.hp)


