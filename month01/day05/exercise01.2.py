"""
作者：周乐
日期：10/09/2019
 列表练习2:在控制台中录入，所有学生成绩.
   输入空字符串，打印(一行一个)所有成绩.
   打印最高分,打印最低分,打印平均分
"""


list_person = []
while True:

    grade = input("请输入学生成绩：")
    if grade == "":
        break
    list_person.append(int(grade)) #int不能放在最开始那，因为后面还要判断是否为空字符串

for item in list_person:  #遍历对象名不能用range了（range是一个整数生成器函数） #重复打印列
    print(item)

print("最高分是%d"%max(list_person))  #max()里面应该是放列表中的某一个，而不是放item每个
print("最低分是%d"%min(list_person))
pin = sum(list_person) / len(list_person)
print("平均成绩是%.1f" %pin)


