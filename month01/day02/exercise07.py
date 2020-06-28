# 练习7：判断年份是否为闰年
# 闰年True：年份能被4整除，但是不能被100整除。
#          或者能被400整除
# 平年False


year = int(input("请输入年份："))

#整除是看余数是否为０
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(result)



