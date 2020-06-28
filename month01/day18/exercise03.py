"""
继续练习day17的函数式编程，并加以运用
练习3：
    在list_helper.py中增加通用的获取最大值方法
    案例1：获取敌人列表中攻击力最大的敌人
    案例2：计算敌人列表中防御力最大敌人
    案例3：计算敌人列表中血量最高的敌人
    步骤：
        实现具体功能／提取变化／提取不变／组合
作者：周乐
日期：12/12/2019
"""

from common.list_helper import *
class Enemy:
    def __init__(self,name,atk,phylactic,hp):
        """
        敌人类
        :param name:名字
        :param atk: 攻击力
        :param phylactic: 防御力
        :param hp: 血量
        """
        self.name = name
        self.atk = atk
        self.phylactic = phylactic
        self.hp = hp
    def __str__(self):
        return "%s--%d--%d--%d"%(self.name,self.atk,self.phylactic, self.hp)

list01 = [
 Enemy("黑衣人",0,500,5000),
 Enemy("灭霸",20000,1000,10000),
 Enemy("大妈",30000,1000,0),
 Enemy("凯多",20000,2000,50000)
]

def max_atk(item):
    return item.atk
def max_phylactic(item):
    return item.phylactic
def max_hp(item):
    return item.hp

re = ListHelper.get_max(list01,lambda item:item.atk)
print(re)
re1 = ListHelper.get_max(list01,lambda item:item.phylactic)
print(re1)
re2 = ListHelper.get_max(list01,lambda item:item.hp)
print(re2)

#同理，自主做一个获取最小元素的方法
re0 = ListHelper.get_min(list01,lambda item:item.atk)
print(re0)
re4 = ListHelper.get_min(list01,lambda item:item.phylactic)
print(re4)
re5 = ListHelper.get_min(list01,lambda item:item.hp)
print(re5)
