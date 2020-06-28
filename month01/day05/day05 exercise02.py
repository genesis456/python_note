"""
作者：周乐
日期：12/09/2019
day05 作业2：

 彩票　双色球：
红球:6个，1 -- 33 之间的整数   不能重复
蓝球:1个，1 -- 16 之间的整数
(1) 随机产生一注彩票[6个红球１个蓝球].

"""
import random
list0 =[]
#6个不重复的红球
while len(list0) < 6:
    # for item in range(6):　　这个时候不能用for来循环了，
       #for只会固定次数，若有重复就也会往里存储，列表中就没有6个不重复的数了
        random_number01 = random.randint(1, 33)
        #如果随机数不存在，则存储．
        if random_number01 not in list0:
            list0.append(random_number01)

#1个蓝球
list0.append(random.randint(1,16))
print(list0)

