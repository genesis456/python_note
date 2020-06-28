"""
作者：周乐
日期：11/09/2019
练习４：
    在列表中［9，25，12，8］，删除大于10的数字
"""

list02 = [9,25,12,8]
for i in range(len(list02)-1,-1,-1):
    if list02[i] > 10:
        list02.remove(list02[i])
print(list02)



list01 = [9,25,12,8]
# for item in range[len(list01)-1,-1,-1]:
#     if item > 10:
#         list01.remove(item)

for i in range(len(list01)-1,-1,-1):  #反向判断，因为删除一个值后，地址不会删，／
    # 后面12会替换上25，导致下一个判断会跳过12
    if list01[i] > 10:
        list01.remove(list01[i])

print(list01)