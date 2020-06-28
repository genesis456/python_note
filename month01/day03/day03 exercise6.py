"""
作者：周乐
日期：03/09/2019
while练习3: 猜数字游戏
游戏运行产生一个1－－100之间的随机数．
让玩家重复猜测，直到猜对为止．
　提示：　　大了
            小了
            　猜对了，总共猜了多少次


"""
#随机数工具（在开头写一次）
import random

#产生一个随机数
random_number = random.randint(1,100)


count = 0
while True:                          #这题卡住半天了，问题在不知道while后面不知道跟什么条件
                                        #解决之后，不知道条件可以用Ｔrue,但一定要跟break,
                                        #否则会出现死循环
    number = int(input("请输入一个数字："))
    count += 1
    if number > random_number:
        print("你猜大了，请再猜一次")
    elif number < random_number:
        print("你猜小了，请再猜一次")
    else:
        print("猜对了，总共猜了",count,"次")
        break