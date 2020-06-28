"""
作者：周乐
日期：11/08/2019
    循环语句
       while (后面跟条件)条件：
            循环体
"""
#死循环：循环条件永远是满足的．
# while True:
#     usd = int(input("请输入美元："))
#     print(usd * 6.9)
#     if input("输入q退出：") == "q" :
#         break  #退出循环体


#练习：使下列代码循环执行，按e键退出．
# season = input("请输入季度：")
# if season == "春":
#     print("１月～３月")
#
# elif  season == "夏":
#     print("４月～６月")
#
# elif season == "秋":
#     print("７月～９月")
#
# elif season == "冬":
#     print("１０月～１２月")
#调试程序

while True :
    season = input("请输入季度：")
    if season == "春":
        print("１月～３月")

    elif season == "夏":
        print("４月～６月")

    elif season == "秋":
        print("７月～９月")

    elif season == "冬":
        print("１０月～１２月")
    if input("输入e键退出：") == "e":
        break


