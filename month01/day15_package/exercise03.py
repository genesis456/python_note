"""
作者：周乐
日期：27/11/2019
异常处理练习：
    定义函数，在控制台中获取成绩的函数.
    要求：如果异常，继续获取成绩，直到得到正确的成绩为止.
         成绩还必须在0--100之间
"""


def get_grade():
    while True:
        grade = input("请输入成绩：")

        try:      #在可能出错的地方加上异常处理方法
            result = float(grade)

        except :        #如果上面出错
            print("输入的不是整数")
            continue
        if 0 <= result <= 100:

            return result

        else:
            print("超过范围")
print(get_grade())







def get_score():
    while True:
        str_result = input("请输入成绩：")
        try:
            score = int(str_result)
        except:
            print("输入的不是整数")
            continue
        if 0 <= score <= 100:
            return score



print(get_score())


