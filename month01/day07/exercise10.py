"""
作者：周乐
日期：22/09/2019
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
练习:矩阵转置  将二维列表的列，变成行，形成一个新列表.
  第一列变成第一行
  第二列变成第二行
  第三列变成第三行
"""
list01 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
# list02 = []
# list04 = []
# list05 = []
# list06 = []
# # 第一列变成第一行  1 5 9 13(索引：00 10 20 30 )
# for i in range(len(list01)):
#     list02.append(list01[i][0])
# list03 = [list02]
#
# #第二列变成第二行  2 6 10 14(索引：01 11 21 31 )
# for i in range(len(list01)):
#     list04.append(list01[i][1])
# list03.append(list04)
#
# #第三列变成第三行   3 7 11 15(索引：02 12 22 32 )
# for i in range(len(list01)):
#     list05.append(list01[i][2])
# list03.append(list05)
#
# #第四列变成第四行
# for i in range(len(list01)):
#     list06.append(list01[i][3])
# list03.append(list06)
# print(list03)
list02 = []    #先创建最外面的大列表
for r in range(len(list01[0])):  #总列数
    line = []   #再创建里面的小列表
    list02.append(line)  #将小列表放进大列表
    for i in range(len(list01)):  #总行数
        line.append(list01[i][r])  #取出每行对应的每列

print(list02)



