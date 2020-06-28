"""
作者：周乐
日期：12/09/2019
day05 作业2：
    计算列表中最小值(不使用min)．
"""

list01 = [25,12,75,9]
min_value = list01[0]
for item in list01:
    if min_value > item:
        min_value = item
print(min_value)



