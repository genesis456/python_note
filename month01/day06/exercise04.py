"""
作者：周乐
日期：14/09/2019
    元组练习:在控制台中录入日期(月日)，计算这是这一年的第几天.
    例如：３月５日
         1月天数 + 2月天数 + 5

         5月8日
         1月天数 + 2月天数 +3月天数 + 4月天数+ 8

"""

month = int(input("请输入月份："))
day = int(input("请输入日："))
if month < 1 or month > 12:
    print("输入有误")
else:
    day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_day = 0
    for i in range(month-1):   #循环每个月的次数（获取元组里的索引）
        total_day += day_of_month[i]  #累加的是元组里的索引
    total_day += day
    print("是这年的第%d天" % total_day)
#方式：2  #利用sum求和函数和切片结合更容易
    sum_day = sum(day_of_month[:month-1])
    sum_day += day
    print("是这年的第%d天" % sum_day)




