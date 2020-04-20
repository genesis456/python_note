# 练习3
#在控制台中获取分钟
#        再获取小时
#        再获取天数
#        计算总秒数

minute = int(input("请输入分钟："))
hour = int(input("请输入小时："))
day = int(input("请输入天数："))
second = minute * 60 + hour * 3600 + day * 24 * 3600
print("总秒数:",second)

