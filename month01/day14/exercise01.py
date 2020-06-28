"""
# 练习：创建Enemy类对象，将对象打印在控制台中(格式自定义)
#      克隆Enemy类对象，体会克隆对象变量的改变不影响原对象。

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
"""

class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "他是%s,血量是%d,攻击力是%d,防御力是%d"%(self.name,self.hp,self.atk,self.defense)

    def __repr__(self):
        return "Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)

c1 = Enemy("史莱克",5000,500,300)
re = str(c1)
print(re)
print(repr(c1))
s1 = eval(repr(c1))
s1.name = "小明"
print(c1.name)
