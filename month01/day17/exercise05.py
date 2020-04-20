"""

"""
# 1. 使用生成器函数实现以上3个需求
# 2. 体会函数式编程的"封装"
#    将三个函数变化点提取到另外三个函数中.
#    将共性提取到另外一个函数中
# 3. 体会函数式编程的"继承"与"多态"
#    使用变量隔离变化点,在共性函数中调用变量.
# 4. 测试(执行上述功能)

list01 = [43, 4, 5, 5, 6, 7, 87]


# 需求1:在列表中查找所有偶数
# def find01():
#     for item in list01:
#         if item % 2 == 0:
#             yield item
#
# for item in find01():
#     print(item)
#
# # 需求2:在列表中查找所有大于10的数
# def find02():
#     for item in list01:
#         if item>10:
#             yield item
#
# for item in find02():
#     print(item)
#
# # 需求3:在列表中查找所有范围在10--50之间的数
# def find03():
#     for item in list01:
#         if 10<item<50:
#             yield item
#
# for item in find03():
#     print(item)
print("－－－－－－－－以上代码不优雅，有重复代码－－－－－－－－－")

#"封装"
def change_point1(item):
    return item % 2 == 0
def change_point2(item):
    return item>10
def change_point3(item):
    return 10<item<50

#"继承"（隔离变化点，不能直接调上面），在面向对象中是用父类隔离，函数式编程则是用变量隔离change
def find(change):
    for item in list01:
        # "多态"
        # 调用:具体条件的抽象
        # 执行:具体条件的函数

        if change(item):   #调用传入进来的参数，（执行具体函数时要加括号带参数）
            yield item

for item in find(change_point1):   #将需要的变化点函数作为参数传进去不用带括号
    print(item)
for item in find(change_point2):
    print(item)
for item in find(change_point3):
    print(item)

