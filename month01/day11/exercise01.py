"""
日期：5/09/2019
作者：周乐
demo01封装方法练习1：
        定义敌人类(姓名，攻击力10 -- 50，血量100 -- 200)
   创建一个敌人对象，可以修改数据，读取数据
"""
class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        # self.__atk = atk
        self.set_atk(atk)
        # self.__hp = hp
        self.set_hp(hp)


    def get_atk(self):    #获取外部改好的数据
        return self.__atk  #　将改好的参数返回


    def set_atk(self,value):   #修改数据
        if 10 <= value <= 50:
            self.__atk  = value   #赋值调到上面的函数
        else:
            raise ValueError("超出")


    def get_hp(self):    #读取改好的数据
        return self.__hp  #　将改好的参数返回

    def set_hp(self,value):   #修改数据
        if 100 <= value <= 200:
            self.__hp  = value   #赋值调到上面的函数
        else:
            raise ValueError("超出")


cs = Enemy("巴基",10,150)    #只要开始调进去的数据不在范围也会报错，不执行
cs.set_atk(50)    #如果不改直接写进去，则100不会经过那个判断范围（在上面传参那修改　）
cs.set_hp(120)
print(cs.get_atk())
print(cs.get_hp())




