"""
函数练习3：
定义　根据成绩计算等级　的函数
"""
# score = int(input("请输入成绩："))
# if score > 100 or score < 0:
#     print("输入有误")
# elif 80 <= score:
#     print("你很优秀,继续保持！")
# elif 70 <= score:
#     print("成绩良好，继续加油！")
# elif 60 <= score:
#     print("刚好踩线，你很危险！")
# else:
#     print("不及格诶")

def results_calculate_class(score):
    """

    :param score: 根据成绩计算等级
    :return: 等级
    """
    if score > 100 or score < 0:  #只要程序进入19行，后续程序将不再判断
                                # （那后面的elif可以改成if）
        return "输入有误"
    if 80 <= score:
        return "你很优秀,继续保持！"
    if 70 <= score:
        return "成绩良好，继续加油！"
    if 60 <= score:
       return "刚好踩线，你很危险！"

    return "不及格诶"


re = results_calculate_class(65)
print(re)
