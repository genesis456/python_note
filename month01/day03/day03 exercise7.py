"""
作者：周乐
日期：04/09/2019
while练习4：
    循环根据成绩判断等级，如果录入空字符串则退出程序
    如果成绩录入错误次数达到3，则退出成绩并提示"成绩错误过多"
"""

count = 0
while count < 3:
    str_score = input("请输入成绩：")

    if str_score == "":
        break  #不会执行else语句

    score = int(str_score)
    if score > 100 or score < 0:
        print("输入有误")
        count += 1
    elif 80 <= score:
        print("你很优秀,继续保持！")
    elif 70 <= score:
        print("成绩良好，继续加油！")
    elif 60 <= score:
        print("刚好踩线，你很危险！")
    else:
        print("不及格诶")

else:
    print("成绩错误过多")