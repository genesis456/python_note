"""

在exercise07代码上改进：
    # 字典内嵌字典:
    {
        "张无忌":{"age":28,"score":100,"sex":"男"},
    }
"""

dict02 = {}
while True:
    name = input("请输入姓名：")
    if name == "":
        break
    age = int(input("请输入年龄："))
    score = float(input("请输入成绩："))
    sex = input("请输入性别：")
    dict02[name] = {"age":age,"sex": sex,"score": score} #采用字典嵌套字典,把里面的
    #三个元素都作为值，再给它们附上类似的标签作为键


for key, dict_into in dict02.items():  #dict_into是那三个元素的字典
    print("%s今年%d岁，性别：%s,成绩：%.1f" %
          (key, dict_into["age"], dict_into["sex"], dict_into["score"]))