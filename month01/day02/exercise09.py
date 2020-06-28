""""

温度转换器
　摄氏度 = (华氏度 - 32) / 1.8
　华氏度 = 摄氏度 * 1.8  + 32
  开氏度＝ 摄氏度　＋　273.15
  (1)在控制台中获取华氏度，计算摄氏度。
  （２）在控制台中获取摄氏度，计算华氏度。
  (３)在控制台中获取摄氏度，计算开氏度。
　日期：６／０７／２０１９
"""
# fahrenhite = float(input("请输入华氏度："))
# centigrade = (fahrenhite - 32) / 1.8
# print("摄氏度:",centigrade)
#
#
# centigrade = float(input("请输入摄氏度："))
# fahrenhite = centigrade * 1.8 + 32
# print("华氏度为：",fahrenhite)
#
#
# kelvin = centigrade + 273.15
# print("开氏度:"+str(kelvin))
#



# 在控制台中获取总秒数，计算几小时零几分钟零几秒。
total_second = int(input("请输入秒数："))
# 获取小时总秒数 除以　60　取商表示总分钟数
 #  总分钟数 除以　60　取商表示总小时
hour = total_second // 60 //  60
# 获取分钟(剩下的分钟)
minute = total_second // 60 % 60
# 获取秒
second = total_second % 60

print(hour,"小时",minute,"分钟零",second,"秒")

# a = 1000
# b = a
# a = 5000
# print(b)
#
#
#
# num = 1
# re = num > 1 and input("请输入:") == a
#
# print(a)


