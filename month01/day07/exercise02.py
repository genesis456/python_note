"""
作者：周乐
日期：18/09/2019
字典推导式练习2：
    ［"无忌"，"赵敏"，"周芷若"］[101,102,103]
    －－＞｛"无忌"：101，"赵敏"：102，"周芷若"：103｝　

"""
dict1 = {}
list1 = ["无忌","赵敏","周芷若"]
list2 = [101,102,103]
for item in list1:
    for i in list2:
        dict1[item] = i

print(dict1)





# dict0 ={}
#通过索引同时在多个列表中获取元素
# for i in range(len(list1)):
#     dict0[list1[i]] = list2[i]abcdefce
# print(dict0)

# dict0 = {list1[i]: list2[i] for i in range(len(list1))}
# print(dict0)
#
# #需求：字典如何根据value查找key
# # 解决方案１:键值互换
# dict02 = {value: key for key, value in dict0.items()}
# print(dict02)
# print(dict02[101])
# # 缺点:如果key重复,交换或则丢失数据。
# # 如果需要保持所有数据
# # [(k,v),]
# list02 = [(value, key) for key, value in dict0.items()]
# print(list02)
