"""
作者：周乐
日期：15/09/2019
字典练习2: 在控制台中循环录入学生信息(姓名,年龄,成绩,性别).
　　　如果姓名输入空字符, 则停止录入.
将所有信息逐行打印出来.(字典内嵌列表)
"""

dict02 = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = float(input("请输入成绩："))
    sex = input("请输入性别：")
    dict02[name] = [age, sex, score]  #采用列表嵌套（如果是元组就不能改里面）

for key, list01 in dict02.items():
    print("%s今年%d岁，性别：%s,成绩：%.1f" % (key, list01[0], list01[1], list01[2]))
    #姓名作为键，列表里的三个元素作为值．取出键和值