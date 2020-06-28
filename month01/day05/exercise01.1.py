"""
作者：周乐
日期：10/09/2019
  列表练习１：
    在控制台中循环录入，西游记中你喜欢的人物.
    如果输入空字符串，打印(一行一个)所有人物.

"""

list_person = []   #首先要创建一个空列表
#录入过程
while True:
    str_input = input("西游记中你喜欢的人物：")

    if str_input == "":
        break
    list_person.append(str_input)  #把输入的东西添加到列表中

# 输出过程
for item in list_person: #遍历对象名不能用range了（range是一个整数生成器函数） #重复打印列表中的每一个
    print(item)








