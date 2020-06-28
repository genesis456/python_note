"""
作者：周乐
日期：
进一步熟悉for循环：
"""

#练习１：累加１－－１００的和　　（１＋２+...+100）
sum_value = 0   #用于存储之前的和
for item in range(1,101):   #想加到100，结束值必须是101

    #0 += 1(item)
    #1 += 2
    #3 += 3
    sum_value += item
print(sum_value)

#练习２：累加１－－１００之间的偶数和　　（２＋４＋６＋．．．＋１００）
number = 0
for item in range(2,101,2):   #开始值一定会显示出来，所以需设2，偶数步长为2
    #0 += 2(item)
    #2 += 4(item)
    #6 += 6
    #12 += 8
    number += item
print(number)

#练习３：累加１０－－３６之间的和

number = 0
for item in range(10,37):
    number += item

print(number)

 #如果不懂，断点调试　＋　内存图
