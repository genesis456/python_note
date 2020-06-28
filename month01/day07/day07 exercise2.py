"""
作者：周乐
日期：23/09/2019
day07 作业2
 (扩展)方阵转置.（不用做成函数）
    提示：详见图片.
    list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
"""


#思路解析过程（将每列转换成每行）由于1　5　11　16　最后还是在原来位置，那就先前不用管这几个
"""
#list01[1][0] <->list01[0][1]　　2＜－＞5
#list01[2][0] <->list01[0][2]   3＜－＞9
#list01[3][0] <->list01[0][3]   4＜－＞13

for r in range(1,4):    2＜－＞5　3＜－＞9 4＜－＞13
    #list01[r][0]<->list01[0][r]
    pass
#list01[2][1] <->list01[1][2]
#list01[3][1] <->list01[1][3]
for r in range(2,4):#2 3　　
    # list01[r][1] <->list01[1][r]
    pass
#list01[3][2] <->list01[2][3]
for r in range(3,4):
    # list01[r][2] <->list01[2][r]
    pass

for c in range(1,4):#1 2 3
    for r in range(c,4):
        list01[r][c-1],list01[c-1][r]=list01[c-1][r],list01[r][c-1]

"""

def square_transpose():
    """

    :return: 方阵转置
    """
    for c in range(1, len(list01)):
        for r in range(c, len(list01)):
            list01[r][c-1], list01[c-1][r] = list01[c-1][r], list01[r][c-1]


list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
square_transpose()
print(list01)
