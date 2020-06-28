"""
  作者：周乐
  日期：24/07/2019
  if练习５：
  在控制台中录入一个成绩
  判断等级（优秀／良好／及格／不及格／输入有误）

"""
# score = int(input("请输入成绩："))
# if 80 <= score <= 100:
#     print("你很优秀,继续保持！")
# elif 70 <= score <= 80:
#     print("成绩良好，继续加油！")
# elif 60 <= score <= 70 :
#     print("刚好踩线，你很危险！")
# elif 0 <= score < 60:
#     print("不及格诶")
# else:
#     print("输入有误")

"""
代码优化
"""
score = int(input("请输入成绩："))

if score > 100 or score < 0:
    print("输入有误")
elif 80 <= score:
    print("你很优秀,继续保持！")
elif 70 <= score:
    print("成绩良好，继续加油！")
elif 60 <= score:
    print("刚好踩线，你很危险！")
else:
    print("不及格诶")
