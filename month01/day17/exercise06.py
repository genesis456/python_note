"""
    测试 通用模块list_helper
"""
from common.list_helper import *


class SkillData:
    def __init__(self, id, name, atk_ratio, duration):
        self.id = id
        self.name = name
        self.atk_ratio = atk_ratio
        self.duration = duration

    def __str__(self):
        return "技能数据是:%d,%s,%d,%d" % (self.id, self.name, self.atk_ratio, self.duration)


list_skill = [
    SkillData(101, "乾坤大挪移", 5, 10),
    SkillData(102, "降龙十八掌", 8, 5),
    SkillData(103, "葵花宝典", 10, 2),
]


def condition01(item):
    return item.atk_ratio > 6


def condition02(item):
    return 4 < item.duration < 11


def condition03(item):
    return len(item.name) > 4 and item.duration < 6

# 案例:查找名称是"葵花宝典"的技能.
#     查找编号是101的技能.
#     查找持续时间大于0的技能.

def change_point01(item):
    return item.name == "葵花宝典"
def change_point02(item):
    return item.id == 101
def change_point03(item):
    return item.duration > 0


# generate01 = ListHelper.find_all(list_skill, condition01)
#用lambda匿名函数替换   ListHelper类名去调
generate01 = ListHelper.find_all(list_skill, lambda item : item.atk_ratio > 6)
for item in generate01:
    print(item)
print("----------------")

# re = ListHelper.find(list_skill, change_point01)
#用lambda匿名函数替换　　　　　　　　　　　item表示列表中的每一个元素
re = ListHelper.find(list_skill, lambda item : item.name == "葵花宝典")
print(re)   #调到类中的str方法打印


# 练习:在list_helper.py中,定义通用的查找满足条件的单个对象.
# 案例:查找名称是"葵花宝典"的技能.
#     查找编号是101的技能.
#     查找持续时间大于0的技能.

# 建议:
# 1. 现将所有功能实现
# 2. 封装变化(将变化点单独定义为函数)
#    定义不变的函数
# 3. 将不变的函数转移到list_helper.py中
# 4. 在当前模块测试
print("----------------")
#先按基本思路完成需求，最后优化代码
# def find0():
#     for item in list_skill:
#         if item.name == "葵花宝典":
#             return item
#
# re = find0()
# print(re)
#
# def find01():
#     for item in list_skill:
#         if item.id == 101:
#             return item
#
# re = find01()
# print(re)
#
# def find02():
#     for item in list_skill:
#         if item.duration > 0:
#             yield item
#
# for item in find02():
#     print(item)

# for item in find(change_point01):
#     print(item)


# 需求1:计算技能列表中技能名称大于4个字的技能数量.
# 需求2:计算技能列表中技能持续时间小于等于5的技能数量.
# 步骤:
# 实现每个需求/单独封装变化/定义不变的函数("继承"/"多态")
# 将不变的函数提取到list_helper.py中
"""
def get_count01():
    count_value = 0
    for item in list_skill:
        if len(item.name) > 4:
            count_value +=1
    return count_value

def get_count02():
    count_value = 0
    for item in list_skill:
        if item.duration <= 5:
            count_value +=1
    return count_value

def get_count(func_duration):
    count_value = 0
    for item in list_skill:
        # if item.duration <= 5:
        if func_duration(item):
            count_value +=1
    return count_value
    思路过程
"""
re = ListHelper.get_count(list_skill,lambda item:len(item.name) > 4)
print(re)
re = ListHelper.get_count(list_skill,lambda item:item.duration <= 5)
print(re)