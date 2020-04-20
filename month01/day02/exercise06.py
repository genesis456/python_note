"""
练习6：
在控制台中录入一个四位整数：　　１２３４
计算每位相加和　　　１＋２＋３＋４
显示结果　　　　１０
"""
# str_integer = int(input("请输入四位整数："))
#
# unit01 = str_integer % 10   #获取个位4
#
# unit02 = str_integer // 10 % 10 #获取十位3   1234 // 10->123 % 10 -> 3
#
# unit03 = str_integer // 100 % 10    #获取百位2  1234 // 100->12 % 10 -> 2
#
# unit04 = str_integer // 1000   #获取千位1   1234//1000->1
#
# result = unit01 + unit02 + unit03 + unit04
#
# print("结果为:",result)


#方法２：累加每位（比上述方法优化了很多）
str_integer = int(input("请输入四位整数："))
#个位
result = str_integer % 10
#累加
result += str_integer // 10 % 10   #十位
result += str_integer // 100 % 10   #百位
result += str_integer //1000       #千位

print("结果为:",result)
