"""
4. 在list_helper中增加判断是否存在某个对象的方法.返回值:true/false
   案例1:判断敌人列表中是否存在"成昆"
   案例2:判断敌人列表中是否攻击力小于5或者防御力小于10的敌人.
    步骤:
    实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
    将不变的函数提取到list_helper.py中
    体会：函数式编程的思想("封装，继承，多态")

"""
# class Enemy:
#     pass
# list01 = [
#  Enemy("黑衣人",0,500,5000),
#  Enemy("灭霸",20000,1000,10000),
#  Enemy("大妈",30000,1000,0),
#  Enemy("凯多",20000,2000,50000)
# ]
from homework_day1701 import *
#做什么都是先将其功能做出来
"""
def judge1(list01):
    for item in list01:
        if item.name == "成昆":
            return True
    return False

def judge2(list01):
    for item in list01:
        if item.atk < 5 or item.phylactic < 10:
            return True
    return False
"""
#####程序优化，想向架构师前进，必须想更远＃＃＃＃＃＃
def judge01(item):
    return item.name == "成昆"

def judge02(item):
    return item.atk < 5 or item.phylactic < 10


re = ListHelper.is_exists(list01,lambda item:item.name == "成昆")
print(re)
sc = ListHelper.is_exists(list01,lambda item:item.atk< 5 or item.phylactic < 10)
print(sc)
# print(cd)