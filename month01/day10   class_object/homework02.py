"""
4. 定义敌人类
    --　数据:姓名,血量,基础攻击力,防御力
    --　行为:打印个人信息

   创建敌人列表(至少４个元素),并画出内存图。
   查找姓名是"灭霸"的敌人对象
   查找所有死亡的敌人
   计算所有敌人的平均攻击力
   删除防御力小于10的敌人
   将所有敌人攻击力增加50
"""
class Enemy():

    def __init__(self, name, hp, atk, defense):
        """

        :param name: 姓名
        :param hp: 血量
        :param atk: 攻击力
        :param defense: 防御力
        """

        self.name = name
        self.hp = hp
        self.aggressivity = atk
        self.defense = defense

    def print_message(self):
        print("敌人是%s,血量为%d,攻击力为%d,防御力是%d"
              %(self.name, self.hp,self.aggressivity,self.defense))

list01 = [
 Enemy("黑衣人",0,500,5000),
 Enemy("灭霸",20000,1000,10000),
 Enemy("大妈",30000,1000,9),
 Enemy("凯多",20000,2000,50000)
]

def find01():     #查找姓名是"灭霸"的敌人对象
    for item in list01:
        if item.name == "灭霸":
            return item

s0 = find01()
# 返回值为None
# 所以可以判断不是空，再调用其实例方法.
# if e01 != None:
if s0:
    s0.print_message()
else:
    print("没找到")

def find02():   #查找所有死亡的敌人
    list03 = []
    for i in list01:
        if i.hp == 0:
            list03.append(i)
            return list03

se = find02()
for item in se:
    item.print_message()  #调回上面打印　

# 计算所有敌人的平均攻击力
def calculate01():
    stk = 0
    for item in list01:
        stk += item.aggressivity
    return stk/len(list01)

print(calculate01())

# 删除防御力小于10的敌人
def delete01():
    #倒序删除　3，2，1，0
    for item in range(len(list01)-1,-1,-1):
        if list01[item].defense < 10:
            del list01[item]

vs = delete01()
for i in list01:
    i.print_message()

# 将所有敌人攻击力增加50
def add():
    for item in list01:
        item.aggressivity += 50

xs = add()
for i in list01:
    i.print_message()