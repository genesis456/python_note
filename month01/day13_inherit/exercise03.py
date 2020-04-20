"""
    手雷炸了，可能伤害敌人/玩家的生命.
             还可能伤害未知事物(鸭子.房子....)
    要求：增加了新事物，不影响手雷。
    体会：继承的作用
         多态的体现
         设计原则
            开闭原则
            单一职责
            依赖倒置
    画出设计图

"""

class Granade:
    """
    手雷
    """
    def __init__(self, atk):  #atk 定义一个爆炸伤害
        self.atk = atk

    def explode(self, damage_target):  #damage_target定义传进来的是玩家对象还是敌人对象
        # 如果传入的不是子类，则报错.
        if not isinstance(damage_target, Damageable):
            raise ValueError("不是Damageable的子类")

        print("爆炸")
        # 多态:
        # 调用父类代表(玩家/敌人.....)的可以受伤者.
        # 执类行子(具体玩家/敌人.....)
        damage_target.damage(self.atk)  #调用敌人（或玩家）里的受伤行为


class Damageable:
    """
        可以受伤的
        继承:统一多个子类的概念，隔离变化。
    """

    def damage(self, value):
        # 如果子类不重写，则异常。
        raise NotImplementedError()    #如果子类和父类中的构建函数（def damage(self, value)）不一样就执行报错代码


# ------------------------------
class Player(Damageable):
    """
    玩家
    """
    def __init__(self, hp):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        print("玩家受伤啦")
        print("碎屏")


class Enemy(Damageable):
    """
    敌人
    """
    def __init__(self, hp):
        self.hp = hp

    def damage2(self, value):   #子类的成员和父类的成员不相同，就执行了父类中的报错程序
        self.hp -= value
        print("敌人受伤喽")
        print("头顶爆字")


g01 = Granade(100)
e01 = Enemy(200)
p01 = Player(300)
# g01.explode(e01)    #由于在继承中，子类和父类的方法不同，所以执行了报错程序
g01.explode(p01)