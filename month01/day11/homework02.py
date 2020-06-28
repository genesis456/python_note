"""＃很重要（面试类题）
 请用面向对象思想，描述以下场景：
    玩家(攻击力)攻击敌人(血量)，敌人受伤(掉血)，还可能死亡(掉装备，加分)。
    敌人(攻击力)攻击玩家，玩家(血量)受伤(掉血/碎屏),还可能死亡(游戏结束)。
    体会：类区别行为的不同
"""
"""
体会两个类之间的相互调用
"""
#玩家类

class Game_player:
    def __init__(self,atk,hp):
        self.atk = atk
        self.hp = hp

    #玩家攻击
    def attack(self,other):
        """
        玩家攻击
        :param other: 敌人受伤对象

        """
        print("玩家攻击敌人")
        other.bruise(self.atk)

    #玩家受伤
    def bruise(self,value):
        """
        玩家受伤
        :param value: 玩家每次受的伤害
        """
        print("玩家受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    # 私有的死亡方法（隐藏的，不能修改的＿＿）
    def __death(self):
        # 死亡的逻辑
        print("掉血")
        print("碎屏")
        print("游戏结束")

#敌人类
class Enemy:
    def __init__(self,hp,atk):
        self.hp = hp
        self.atk = atk

    #敌人受伤
    def bruise(self,value):
        """
        敌人受伤
        :param value: 敌人每次受的伤害
        """
        print("敌人受伤")
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    # 私有的死亡方法
    def __death(self):
        # 死亡的逻辑
        print("掉血")
        print("掉装备")
        print("加分")

    #敌人攻击玩家
    def attack(self, other):
        print("敌人攻击玩家")
        other.bruise(self.atk)


re01 = Game_player(100,1000)  #攻击力，血量
re02 = Enemy(200,1000)     #血量,攻击力
re01.attack(re02)   #玩家攻击敌人
re02.attack(re01)    #敌人攻击玩家







