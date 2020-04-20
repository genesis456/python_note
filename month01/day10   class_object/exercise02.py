"""
实例成员：
练习１：定义函数，在list01中查找name是"苏大强"的对象．
将名称与年龄打印在控制台中
 """


class Student:   #先做一个类
    def __init__(self, name, age, score, sex):  #数据
        self.name = name
        self.age = age
        self.score = score
        self.sex = sex

    def print_self_info(self):  #行为
        print("%s的年龄是%d,成绩是%d,性别是%s" % (self.name, self.age, self.score, self.sex))


list01 = [
    Student("赵敏", 28, 100, "女"),
    Student("苏大强", 68, 62, "男"),
    Student("明玉", 30, 95, "女"),
    Student("cary", 23, 99, "女"),
    Student("kisc", 24, 90, "女")
]



def find01():
    for item in list01:
        if item.name == "苏大强":
            return item

    #return None        如果没找到，则返回空。而函数返回值默认就是空,所以可以不写.
        #对齐for

st = find01()
print(st.name , st.age)

#练习２：定义函数，在list01中查找是女的学生并打印名字和性别
def find_gril():
    list02 = []
    for item in list01:
        if item.sex == "女":
            list02.append(item)
    return list02

gr = find_gril()
for item in gr:
    print(item.name,item.sex)


#练习3：定义函数，查找年龄　＞＝　30的学生数量
def find03():
    count = 0
    for item in list01:
        if item.age >= 30:
            count+=1
    return count

print(find03())


#练习４:定义函数，将list01中所有学生成绩归零
def score_zero():
    for item in list01:
        item.score = 0

score_zero()
for item in list01:
    print(item.name,item.score)

#练习5:定义函数，获取list01中所有学生名字
def input_name():
    list04 = []
    for item in list01:
        list04.append(item.name)
    return list04
re = input_name()
print(re)

#练习6:定义函数，在list01中查找年龄的最大学生对象
def max_age():
    max_stu = list01[0]
    for item in range(1,len(list01)):
        if max_stu.age < list01[item].age:
            max_stu = list01[item]
    return max_stu


lc = max_age()
lc.print_self_info()