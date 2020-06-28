"""
    包

python程序结构
    文件夹  ---- 项目根目录
        包
            模块
                类
                    函数
                        语句
    练习：my_project
"""

# form 包.模块 import 成员
from package01.module_a import fun01
fun01()
#
# form 包.包.模块 import 成员
from package01.package02.module_b import fun02 #模块被导入时，会自上而下编译
                              # (所以会先执行module_b中的程序，然后再调到fun02中执行)
fun02()

# import package01.module_a as pm
# pm.fun01()