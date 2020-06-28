"""
(扩展)计算一个字符串中的字符以及出现的次数.
# 思想：
# 逐一判断字符出现的次数.
# 如果统计过则增加１，如果没统计过则等于１.

abcdefce
a 1
b 1
c 2
d 1
e 2
f 1

"""

dict1 ={}
str00 = "abcdefcea"
for item in str00:
    if item not in dict1:   #如果在字典中不存在ｉtem中的某元素，就和那元素分别作为键值放入字典
        dict1[item] = 1
    else:
        dict1[item] +=1

print(dict1)
