"""
    列表推导式
    练习:exercise01.py
"""

# # 将list01中所有元素,增加１以后存入list02中.
# list01 = [5, 56, 6, 7, 7, 8, 19]
# # list02 = []
# # for item in list01:
# #     list02.append(item + 1)
# list02 = [item + 1 for item in list01]
# print(list02)
# # 将list01中大于１０元素,增加１以后存入list02中.
# # list02 = []
# # for item in list01:
# #     if item >10:
# #         list02.append(item + 1)
# list02 = [item + 1 for item in list01 if item > 10]

list01 = [800,[1000,500]]
list02 = list01[:]
# list02 = list01.copy()
list01[1][0] = 900
print(list02[1][0])


