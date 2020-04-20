"""
日期：16/12/2019
作者：周乐
内置高阶函数练习：
    1.([1,1,],[2,2],[3,3,3,3])
        获取元组中，长度最大的列表
    2.根据敌人列表，获取所有敌人的姓名与血量与攻击力
    3.在敌人列表中，获取攻击力大于100的所有活人
    4.根据防御力对敌人列表进行降序排列
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


# 1.([1,1,],[2,2],[3,3,3,3])
#         获取元组中，长度最大的列表
tuple01 = ([1,1,],[2,2],[3,3,3,3])
re = max(tuple01,key = lambda item:len(item))
print(re)

#建议改写day17/exercise02


# 根据敌人列表，获取所有敌人的姓名与血量与攻击力
re = map(lambda item:(item.name,item.atk,item.hp),list01)
for item in re:
    print(item)


# 3.在敌人列表中，获取攻击力大于100的所有活人
re = filter(lambda item:item.hp>0 and item.atk >100,list01)
for item in re:
    print(item)

# 4.根据防御力对敌人列表进行降序排列
re = sorted(list01,key =lambda item :item.phylactic,reverse = True)
for item in re:
    print(item)

###总结：　还是用自己做的方法，可以跨语言