"""
作者：周乐
日期：18/09/2019
字典推导式练习1：
    ［"无忌"，"赵敏"，"周芷若"］
    －－＞｛"无忌"：2，"赵敏"：2，"周芷若"：3｝　＃数字是字符串长度

"""

list1 = ["无忌","赵敏","周芷若"]
# dict1 = {}
# for item in list1:
#     dict1[item] = len(item)
# print(dict1)
dict1 = {item : len(item) for item in list1}
print(dict1)