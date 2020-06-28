"""
作者：周乐
日期：05/09/2019

    ｆｏｒ循环练习：随机加法考试
            随机产生两个数字（１－－１０）
            在控制台中获取两个数相加的结果
            如果用户输入正确得１０分
            总共３道题，最后输出得分
            　例如："请输入８＋３＝？"　10   不得分
            　　　　"请输入4＋３＝？"　7　　　得１０分
                　"请输入４＋４＝？"　　8　　　得１０分
                "总分是２０分"
"""


import random


score = 0
for item in range(3):
    #产生一个随机数
    random_number01 = random.randint(1,10)  #第一个随机数

    random_number02 = random.randint(1,10)  #第二个随机数

    input_number = int(input("请输入"+ str(random_number01)+"+"+str(random_number02)+"="))
     #将格式打印到控制台上
    if input_number == random_number01 + random_number02: #如果用户回答正确就执行下一条
        score += 10  #满足就加10

print("总分:",score)

#没做出来，多看，调试理解

