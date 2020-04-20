"""
猜数字游戏2
    最多猜3次，如果猜对提示"猜对了，总共猜了？次"
    如果超过次数，提示"游戏结束"

"""


#随机数工具（在开头写一次）
import random

#产生一个随机数
random_number = random.randint(1,100)


count = 0
while count < 3:                          #这题卡住半天了，问题在不知道while后面不知道跟什么条件
                                        #解决之后，不知道条件可以用Ｔrue,但一定要跟break,                                        #否则会出现死循环
    number = int(input("请输入一个数字："))
    count += 1
    if number > random_number:
        print("你猜大了，请再猜一次")
    elif number < random_number:
        print("你猜小了，请再猜一次")
    else:
        print("猜对了，总共猜了",count,"次")
        break  #猜对了就退出循环体

else:  #while的条件不满足
    #三次以外
    print("游戏结束")