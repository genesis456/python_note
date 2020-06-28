"""
    练习1：
        将day11/day10_exercise/exercise01.py中的
        Vector2和DoubleListHelper定义到
          double_list_helper.py模块中.
    练习2:
        在exercise03.py模块中，实现
        (1)在二维列表中，获取13位置，向左，3个元素

        (2)在二维列表中，获取22位置，向上，2个元素

        (3)在二维列表中，获取03位置，向下，2个元素
    要求：使用三种导入方式
    体会：哪一种更合适。
"""


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]

#方式1（适合函数方法多的时候）
# import double_list_helper as helper   #太长了，用别名替代
# re = helper.DoubleListHelper.get_elements(list01,helper.Vector2(1, 3),helper.Vector2.left(),3)
# print(re)

#方式2：　（）三种模块调用方法看情况调用
# from double_list_helper import DoubleListHelper
# from double_list_helper import Vector2
# cs = DoubleListHelper.get_elements(list01,Vector2(2,2),Vector2.up(),2)
# print(cs)

#方式3：(个人感觉第三种简便，但仅对于熟悉的模块，不然容易冲突)
from double_list_helper import *
cx = DoubleListHelper.get_elements(list01,Vector2(0,3),Vector2.down(),2)
print(cx)