"""
作者：周乐
日期：05/12/2019
生成器练习
# 练习:1. 获取列表中所有字符串
#     2. 获取列表中所有小数
# 要求:分别使用生成器函数/生成器表达式/列表推导式完成.
"""
# 练习:1. 获取列表中所有字符串
#方法1：
list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]
def find_str():
    for item in list01:
        if type(item) == str:
            yield item

re = find_str()
for item in re:
    print(item)
#方法2：
re = (item for item in list01 if type(item) == str)
for item in re:
    print(item)

#方法3：
re = [item for item in list01 if type(item) == str]
for item in re:
    print(item)

#2. 获取列表中所有小数
#方法1：
list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]
def find_float():
    for item in list01:
        if type(item) == float:
            yield item

for item in find_float():  #简写
    print(item)
#方法2：
re = (item for item in list01 if type(item) == float)
for item in re:
    print(item)

#方法3：
re = [item for item in list01 if type(item) == float]
for item in re:
    print(item)