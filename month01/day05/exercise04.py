"""
作者：周乐
日期：11/09/2019
在列表中[54,25,12,42,35,17],选出最大值（不使用max）
"""

max_value1 = 0
list01 = [54,25,12,42,35,17]
for item in list01:
    if max_value1 < item:
        max_value1 = item

print(max_value1)


