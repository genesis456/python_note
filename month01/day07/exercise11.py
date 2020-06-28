"""
　　　列表推导式嵌套
练习:列表的全排列
[“香蕉”,"苹果","哈密瓜"]
[“可乐”,"牛奶"]
"""
list01 = ["香蕉","苹果","哈密瓜"]
list02 = ["可乐","牛奶"]
# for r in list01:
#     for c in list02:
#         list04.append(r+c)
list04 = [r+c for r in list01 for c in list02]
print(list04)

