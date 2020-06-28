"""
作者：周乐
日期：23/09/2019
day07 作业1

定义在控制台中打印二维列表的函数
[
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]

1 2 3 44
4 5 5 5 65 6 87
7 5

"""
def print_two_dimensional(list_v):
    """
    打印二维列表
    :param list_v: 需要打印的二维列表
    """

    for line in list_v:
        for r in line:
            print(r, end=" ")  #end遍历不换行，＂＂中间加空格
        print()   #print()打印空白，终结上面end的作用(行与行之间要换行)
list01 = [
    [1,2,3,44],
    [4,5,5,5,65,6,87],
    [7,5]
]
print_two_dimensional(list01)