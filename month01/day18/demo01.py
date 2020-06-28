"""
内置高阶函数
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

#1.filter:根据条件筛选可迭代对象中的元素，返回值为新可迭代对象
#需求:获取所有死人
for item in ListHelper.find_all(list01,lambda item:item.hp==0):
    print(item)

re = filter(lambda item:item.hp == 0,list01)
for item in re:
    print(item)

# #2.通用的筛选方法
# #需求：获取所有敌人的姓名
for item in ListHelper.screen(list01,lambda item : item.name):
    print(item)

#
re = map(lambda item:item.name,list01)
for item in re:
    print(item)

#3.max
#需求：获取血量最大的敌人
print(ListHelper.get_max(list01,lambda item:item.hp))
print(max(list01,key =lambda item:item.hp))

#4.min:获取最小值
#同上


#5排序方法
#内部直接修改列表，使用是无需通过返回值获取数据
ListHelper.ascending_order(list01,lambda item :  item.atk)
for item in list01:
    print(item)

#（使用内置函数时）内部返回新列表，使用时必须获取返回值
re = sorted(list01,key =lambda item :  item.atk)#第一个是可迭代对象，后面一个是命名关键字
for item in re:
    print(item)

#该函数支持降序
re = sorted(list01,key =lambda item :  item.atk,reverse = True)
#使用ctrl+p查看参数信息
# 第一个是可迭代对象，第二个是命名关键字，最后一个reverse反转的意思（默认值是Ｆlase，不反转的意思）
#reverse = True（反转）
for item in re:
    print(item)






























