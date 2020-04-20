"""
作者：周乐
日期：04/09/2019
初识for循环：
for : 适合执行预订次数．
while:适合根据条件循环执行．
"""

#for 变量　in 可迭代对象：
#   循环体


str01 = "wfasfas"

#item 存储的是字符串中每个字符的地址
for item in str01:
    print(item)

    #整数生成器：range(开始值，结束值，间隔（是开始值与结束值的间隔，也叫步长））
    #for + range : 更善于执行预订次数
for item in range(1,5,1):
    print(item)  #结果输出的是1　2　3　4　（不会等于结束值）

for item in range(1,5,2):
    print(item) #间隔为２，输出的结果是１　３

for item in range(1,5):
    print(item) #要是没有间隔，默认是１


for item in range(5):
    print(item) #开始值也可以省略，默认是0


#需求：折纸10次
thickness = 0.0001
for i in range(10):
    thickness *= 2
print(thickness)






