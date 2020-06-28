# 记录from 包 import * 语句需要导入的模块
# 案例：
# my_ project /
# main.py
# common/
#     __init__.py
# 	double_list_helper.py
# 	list_helper.py
#     skill_system/
#         __init__.py
#         skill_deployer.py
# 		skill_manager.py
# 练习:

def fun1():
    print(123456)


# 要求：在所有的调用过程中，要包含函数、类、实例方法、静态方法。

# 1.	在main.py中调用skill_deployer.py。
#方法1：
from skill_system.skill_deployer import *
fun02()
# #方法2：
# import skill_system.skill_deployer as tr
# tr.fun02()

