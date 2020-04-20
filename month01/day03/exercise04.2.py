"""
作者：周乐
日期：07/08/2019
练习2（exercise04所学知识）：
    在控制台中录入一个年份，
    如果是闰年，给变量day赋值２９，否则赋值２８．
"""
year = int(input("请输入一个年份："))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
#if year % 4 == 0(可以逆向思维　if not year % 4 但没有做到可读性，不建议采纳)
#==可以去掉用not代替，但!=不能用取代或直接加not，否则会是双重否定了（即肯定）
print(day)



















