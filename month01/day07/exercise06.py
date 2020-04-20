"""
    双for循环
"""

for r in range(3):
    for i in range(4):

        print("*", end=" ")   #end是将遍历的由列转成行
    print()

"""
*#*#*#
*#*#*#
*#*#*#
*#*#*#
"""

#外层循环控制行
for r in range(4):
    #内层循环控制列
    for c in range(6):
        if c % 2 == 0:  #通过索引判断*在偶数位置
            print("*", end=" ")
        else:
            print("#", end= " ")
    print()

"""
    *
    **
    ***
    ****

"""


for r in range(4):      #0 1 2
    for c in range(r+1):  #1 2 3
        print("*",end= "")
    print()