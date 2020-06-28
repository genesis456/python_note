"""
继续练习day17的函数式编程，并加以运用
练习2：
    在list_helper.py中增加通用的筛选方法
    案例1：获取敌人列表中所有敌人的名称
    案例2：计算敌人列表中所有敌人的攻击力
    案例3：计算敌人列表中所有敌人的名称和血量
    步骤：
        实现具体功能／提取变化／提取不变／组合
作者：周乐
日期：11/12/2019
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

def screen_name(item):
    return item.name
def screen_atk(item):
    return item.atk
def screen_name_hp(item):
    return (item.name,item.hp)
re = ListHelper.screen(list01,lambda item:item.name)
for item in re :
    print(item)
for item in ListHelper.screen(list01,lambda item:item.atk):
    print(item)
for item in ListHelper.screen(list01,lambda item:(item.name,item.hp)):
    print(item)
