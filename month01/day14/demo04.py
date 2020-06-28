"""
    模块
    17:00
    练习:exercise03.py

    #####  调用模块时，模块必须放在同一个文件夹中，
         并将文件夹标记（点击文件夹－－＞鼠标右键－－＞
      ＭARK Directory as -->Sources Root）,然后再
        进行导入模块就会出现提示了

"""
# 导入方式1
# 本质：使用变量名module01关联模块地址
# import module01
# module01.fun01()　　#直接用模块．方法
# my02 = module01.MyClass02()　　　#类需要用模块．类赋给对象去调
# my02.fun02()

# as 为导入的成员其另外一个名称
import module02 as m01         #将模块定义一个别名
m01.fun01()
my02 = m01.MyClass02()
my02.fun02()

# 导入方式2
# 本质：将指定的成员导入到当前模块作用域中
# 小心：导入进来的成员不要和当前模块成员名称相同
# from module01 import fun01　　　#导入模块的指定成员（但不要和当前模块的成员名称相冲突，否则就近执行）
# from module01 import MyClass02
#
# def fun01():
#     print("当前模块fun01")
#
# fun01()
# my02 = MyClass02()
# my02.fun02()

# 导入方式3
# 本质：将指定模块的所有成员导入到当前模块作用域中
# 小心：导入进来的成员和其他模块成员冲突
from module02 import *

fun01()
my02 = MyClass02()
my02.fun02()
