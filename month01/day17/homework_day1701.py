"""
作业:
1. 三合一
2. 当天练习独立完成
3. 定义敌人类(姓名,攻击力,防御力,血量)
   创建敌人列表,使用list_helper实现下列功能.
   (1) 查找姓名是"灭霸"的敌人
   (2) 查找攻击力大于10的所有敌人
   (3) 查找活的敌人数量
5. 阅读：
　　　HeadFirst设计模式
　　　重构　
作者：周乐
日期：08/12/2019
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
# (1) 查找姓名是"灭霸"的敌人
ret = ListHelper.find(list01,lambda item:item.name == "灭霸")
print(ret)   #要打印格式，就要在类中创建str方法
# (2) 查找攻击力大于10的所有敌人
re = ListHelper.find_all(list01,lambda item:item.atk > 10)
for temp in re:
    print(temp)
#(3) 查找活的敌人数量
temp = ListHelper.get_count(list01,lambda item:item.hp > 0)
print(temp)

