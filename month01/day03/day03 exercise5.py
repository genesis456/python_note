"""
作者：周乐
日期：03/09/2019
while练习2：
　　 一张纸的厚度是0.01毫米
请计算对折多少次，超过珠穆朗玛峰8844.43米
"""

thickness = 0.01 / 1000

count = 0
while thickness < 8844.43:   #出现的问题：不知道＂多少次＂在哪计数
    count +=1
    thickness *= 2
    #print(thickness)   #可以查看过程
print(count)
#编程思维按人的定向思维走，然后自行组合

