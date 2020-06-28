"""
作者：周乐
日期：22/09/2019
函数练习2:定义在控制台中打印一维列表的函数.
例如：[1,2,3]-->1 2 3  每个元素一行
"""
def number(list_x):     #形参
    """
    打印列表
    :param list_x: 　目标列表

    """
    for item in list_x:
        print(item)
list01 = [1,2,3]   #不能将数值类的参数放入函数中，不然就没法做到随意修改
number(list01)