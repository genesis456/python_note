
"""
    函数返回值 语法
"""
# 参数：调用者传递给定义者的信息
# 返回值：定义者传递给调用者的结果
def fun01(a):
    print("fun01执行喽")
    return 20   # 作用：1. 返回结果  2.退出方法
    print("fun01又执行喽")

# F8 逐过程　（调试时跳过方法）
# F7 逐语句  （调试时进入方法）
re = fun01(10)
print(re)

# 无返回值函数
def fun02(a):
    print("fun01执行喽")
    # return None

re = fun02(100)
print(re)
"""
    函数返回值　应用
    
"""


# 设计思想：分而治之
#         干一件事

# 需求：定义两个数字相加的函数
# def add():
#     1. 获取数据
#     number01 = int(input("请输入第一个数字："))
#     number02 = int(input("请输入第二个数字："))
#     2. 逻辑计算
#     result = number01 + number02
#     3. 显示结果
#     print(result)
#
# add()

def add(number01, number02):
    # 逻辑处理
    return number01 + number02


# 调用者提供数据
number01 = int(input("请输入第一个数字："))
number02 = int(input("请输入第二个数字："))
result = add(number01, number02)
# 调用者负责显示结果
print("结果是:" + str(result))

# F7逐语句  （调试时进入方法(进入函数的执行结果)）
