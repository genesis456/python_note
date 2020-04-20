"""
继续练习day17的函数式编程，并加以运用
练习1：
    在list_helper.py中增加通用的求和方法
    案例1：计算敌人列表中所有敌人的总血量
    案例2：计算敌人列表中所有敌人的总攻击力
    案例3：计算敌人列表中所有敌人的总防御力
    步骤：
        实现具体功能／提取变化／提取不变／组合

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


# def sum_hp(lager):
#     sum_value = 0
#     for item in lager:
#         sum_value +=item.hp
#     return sum_value
#
# re = sum_hp(list01)
# print(re)
# def sum_atk(lager):
#     sum = 0
#     for item in lager:
#         sum +=item.atk
#     return sum
#
# def sum_phylactic(lager):
#     sum = 0
#     for item in lager:
#         sum += item.phylactic
#     return sum
# 整理，将变化和不变化的分别封装起来

def add_hp(item):
    return item.hp
def add_atk(item):
    return item.atk
def add_phylactic(item):
    return item.phylactic

print(ListHelper.add_sum(list01,lambda item:item.hp))
print(ListHelper.add_sum(list01,lambda item:item.atk))
print(ListHelper.add_sum(list01,lambda item:item.phylactic))