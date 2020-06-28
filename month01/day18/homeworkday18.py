"""
作业：
1.三合一
2.当天练习独立完成（list_helper.py)
3.在list_helper.py中新增以下功能：
    (1)获取最小值
    (2）降序排列
    (3)根据指定条件删除元素
        案例：在敌人列表中，删除所有死人.
        案例：在敌人列表中，攻击力小于50的所有敌人.
        案例：在敌人列表中，防御力大于100的所有敌人．
4.阅读"面向对象答辩优胜者"文档
    总结出属于自己的话术，以便就业准备简历时使用（介绍项目）
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
"""
#
#(3)根据指定条件删除元素
 #       案例：在敌人列表中，删除所有死人.
def del01():
    #删除要反向索引　3　2　1　0
    for i in range(len(list01)-1,-1,-1):
        if list01[i].hp == 0:
            del list01[i]

 #       案例：在敌人列表中，攻击力小于50的所有敌人.
def del02():
    # 删除要反向索引　3　2　1　0
    for i in range(len(list01) - 1, -1, -1):
        if list01[i].atk<50:
            del list01[i]
#案例：在敌人列表中，防御力大于100的所有敌人．
def del03():
    #删除要反向索引　3　2　1　0
    for i in range(len(list01)-1,-1,-1):
        if list01[i].phylactic>100:
            del list01[i]

def temp_del(item):
    return item.hp == 0
def temp_del0(item):
    return item.atk<50
def temp_del1(item):
    return item.phylactic>100

def delete_all(fun_delete):
    for i in range(len(list01)-1,-1,-1):
        # if list01[i].phylactic>100:
        if fun_delete(list01[i]):
            del list01[i]
delete_all(temp_del0)
for item in list01:
    print(item)
"""
ListHelper.delete_all(list01,lambda item :item.hp==0)
for item in list01:
    print(item)
print("------------")
ListHelper.delete_all(list01,lambda item :item.atk<50)
for item in list01:
    print(item)
print("------------")
ListHelper.delete_all(list01,lambda item :item.phylactic>100)
for item in list01:
    print(item)