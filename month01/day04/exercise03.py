"""
作者：周乐
日期：06/09/2019

在控制台中获取一个整数，判断是否为素数
素数：只能被1和自身整除的正数　　例：3　3/1＝3（能被１整除）　3/3＝1　所以3是素数
思路：排除法，使用２到当前数字之间的正数判断，如果存在被整除，则不是素数
例如：判断９
        能否被２－－８之间的数字整除，其中３可以，所以不是素数
    判断８：
        能否被２－－７之间的数字整除，其中２可以，所以不是素数
    判断７：
        能否被２－－６之间的数字整除，其中没有，所以是素数
2　3　5　7　11　13　15　．．．
"""

# －－－－思路过程－－－－－
# 11
# 2－－10之间的数字整除
# if 11 % 2 == 0:
#     print("不是素数")
#
# if 11 % 3 == 0:
#     print("不是素数")
#
# if 11 % 4 == 0:
#     print("不是素数")
# print("是素数")
# 只需将2到10循环一遍就行了

value = int(input("请输入一个整数："))
if value <= 1:
    print("不是素数")
else:
    for item in range(2,value):  #判断value之间的数字，能否整除value

        if value % item == 0:
            print("不是素数")
            break  #如果检测到一个不是素数，后面的就不用判断了(不然就每个都会输出一次)
    else:
        print("是素数")
