"""


continue语句练习：
    累加１０－５０之间个位不是2，5，9的整数
"""

number = 0
for item in range(10,51):
     unit = item % 10
     #个位是2，5，9的整数，就用continue跳过
     if unit == 2 or unit == 5 or unit == 9:
         continue
     number += item

print(number)

