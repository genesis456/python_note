#定义方阵转置函数


def square_matrix_transpose(list01):
    """
   方阵转置
   :param list01: 二维列表
    """
    for c in range(1, len(list01)):      #1,      2,   3
        for r in range(c, len(list01)):#(1,2,3),(2,3),(3)
            list01[r][c-1], list01[c-1][r] = list01[c-1][r], list01[r][c-1]


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]


square_matrix_transpose(list01)    #传入的是可变对象，所以不用返回传过来
print(list01)
#矩阵转置的转置就是原矩阵
square_matrix_transpose(list01)    #传入的是可变对象，所以不用返回传过来
print(list01)