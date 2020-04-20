"""
定义函数　根据年月，　计算有多少天．考虑闰年29天，平年28天
"""
# 不建议方法的返回值类型可能是多种# bool  int
# def count_days(year,month):
#
#     if month < 1 or month > 12:
#         return "输入有误"
#     if month == "2":
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return "29天"
#         else:
#             return "有２８天"
#     if month is (4,6,9,11):
#         return "有３０天"
#     return "有３１天"
#
# print(count_days(2019,5))


#将返回的值尽可能一种看得懂的类型
# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:　　　　　　　　＃这段代码违背了函数的设计思想（只干一件事）
                                    #返回天数又判断闰年
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         else:
#             return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

#将另一件事分出来再用一个函数包装
def is_leap_year(year):
    #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #         return True
    #     else:
    #         return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0  #返回是闰年的值

def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28  #再调用前面的函数（函数之间可以互相调用）
    if month in (4, 6, 9, 11):
        return 30
    return 31

print(get_day_by_month(2019,2))