"""
作者：周乐
日期：06/09/2019
初识continue语句
"""

# 累加１－－１００之间，能被５整除的数字
# sum_value = 0
# for item in range(1,101):
#     if item % 5 == 0:
#         sum_value += item
#
# print(sum_value)


"改进上述代码"
sum_value = 0
for item in range(1,101):
    if item % 5 != 0:
        continue
    sum_value += item

print(sum_value)




