"""

# 列表内嵌字典:
[
    {"name":"张无忌","age":28,"score":100,"sex":"男"},
]
"""

list01 = []
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = float(input("请输入成绩："))
    sex = input("请输入性别：")
    dict_into = {"name": name, "age": age, "sex": sex, "score": score}
    list01.append(dict_into)


for name,dict_into in list01:  #dict_into是那三个元素的字典
    print("%s今年%d岁，性别：%s,成绩：%d" %
          ( dict_into["name"],dict_into["age"], dict_into["sex"], dict_into["score"]))
#获取第一个学生信息　　
dict_into = list01[0]
print("第一个是%s今年%d岁，性别：%s,成绩：%d" %
      (dict_into["name"], dict_into["age"], dict_into["sex"], dict_into["score"]))

