"""
继续练习day17的函数式编程，并加以运用
练习4：
    在list_helper.py中增加通用的升序排列方法
    案例1：将敌人列表按照攻击力升序排列
    案例2：将敌人列表按照防御力升序排列
    案例3：将敌人列表按照血量升序排列
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
def order_atk(item):
    return item.atk
def order_phylactic(item):
    return item.phylactic
def order_hp(item):
    return item.hp

ListHelper.ascending_order(list01,lambda item :item.atk)
for item in list01:  #将排序好的列表打印出来
    print(item)
print("-----------------------")
ListHelper.ascending_order(list01,lambda item :item.phylactic)
for item in list01:  #将排序好的列表打印出来
    print(item)
print("-----------------------")
ListHelper.ascending_order(list01,lambda item :item.hp)
for item in list01:  #将排序好的列表打印出来
    print(item)

#降序排列方法
print("-----------------------")
ListHelper.descending_order(list01,lambda item :item.hp)
for item in list01:  #将排序好的列表打印出来
    print(item)