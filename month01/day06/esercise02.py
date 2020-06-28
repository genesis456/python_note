"""
作者：周乐
日期：14/9/2019
练习:使用range生成1--10之间的数字,将数字的平方存入list01中
将list01中所有奇数存入list02
将list01中所有偶数存入list03
将list01中所有偶数大于5的数字增加1后存入list04

"""

# list01 = []
# for item in range(1,11):
#     list01.append(item ** 2)
list01 = [item ** 2 for item in range(1,11)]   
print(list01)

# list02 =[]
# for item in list01:
#     if item % 2 == 1:
#         list02.append(item)
list02 =[item for item in list01 if item % 2 == 1]
print(list02)

list03 = [item for item in list01 if item % 2 == 0]
print(list03)

list04 = [item +1 for item in list01 if item % 2 == 0 and item > 5]
print(list04)