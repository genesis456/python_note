"""
使用property(读取方法，写入方法)对象,将exercise01的练习优化(demo02)
"""
class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk   #这里和普通数据一样，容易方便查看
        self.hp = hp  #self.hp 只是一个变量，真实存储数据的是self.__hp


    def get_atk(self):    #读取改好的数据
        return self.__atk  #　将改好的参数返回
    def set_atk(self,value):   #修改数据
        if 10 <= value <= 50:
            self.__atk  = value   #赋值调到上面的函数
        else:
            raise ValueError("超出")

    # 属性  property对象拦截对age类变量的读写操作
    atk = property(get_atk,set_atk)   #只要上面数据传进来就跳到这,执行括号里的


    def get_hp(self):    #获取外部改好的数据
        return self.__hp  #　将改好的参数返回
    def set_hp(self,value):   #修改数据
        if 100 <= value <= 200:
            self.__hp  = value   #赋值调到上面的函数
        else:
            raise ValueError("超出")

    # 属性  property对象拦截对age类变量的读写操作
    hp = property(get_hp,set_hp)   #只要上面数据传进来就跳到这,执行括号里的

cs = Enemy("巴基",10,150)   #只要开始调进去的数据不在范围也会报错，不执行
cs.atk = 40    #如果不改直接写进去，则100不会经过那个判断范围（在上面传参那修改set　）
print(cs.atk)  #执行到这时，跳到get_  ,将修改完的结果返回来打印
cs.hp = 120  #括号就不要了
print(cs.hp)
