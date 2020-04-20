"""
 将1970年到2050年中的闰年，存入列表．
"""
# 练习7：判断年份是否为闰年
# 闰年True：年份能被4整除，但是不能被100整除。
#          或者能被400整除
# 平年False
# list1 = []
#
# # if result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# for item in range(1970,2051):
#     if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
#         list1.append(item)
# print(list1)

list1 = [item for item in range(1970,2051)
         if item % 4 == 0 and item % 100 != 0 or item % 400 == 0]

print(list1)

