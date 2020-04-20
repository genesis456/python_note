"""
1、创建学生类
    数据：姓名，年龄，成绩，性别 __init__
    行为：打印学生个人信息的方法    实例方法
2、 循环录入学生信息，如果名字是空字符串， 停止录入
3、打印每个学生的信息（调用学生类的打印方法）
4、打印第一个学生的信息
"""
class Studen:

    def __init__(self,name,age,score,sex):
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def data(self):
        print("%s的年龄是%d，成绩为%d，性别%s"%(self.name,self.age,self.score,self.sex))
# st = Studen("周乐",19,98,"男")
# st.data()
list0 = []
while True:
    name = input("请输入学生姓名：")
    if name == "":
        print("录入完毕")
        break
    age = int(input("请输入学生年龄："))
    score = int(input("请输入学生成绩："))
    sex = input("请输入学生性别：")
    list0.append(Studen(name,age,score,sex))

for i in list0:
    i.data()
list0[0].data()