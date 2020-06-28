"""
  作者：周乐
  日期：１９／０７／２０１９
  if练习２：在控制台中录入一个数字
  再录入一个运算符（＋－＊／）最后录入一个数字.
  根据运算符，计算两个数字.
  要求：如果运算符,不是加减乘除，则提示＂运算符有误＂


"""

number01 = float(input("请输入第一个数字："))
operator = input("请输入一个运算符：")
number02 = float(input("请再输入第二个数字："))


if operator == "+":     #切记要用英文运算符，英文运算符比中文小
    print(number01 + number02)

elif operator == "-":
    print(number01 - number02)

elif operator == "*":
    print(number01 * number02)

elif operator == "/":
    print(number01 / number02)

else:
    print("运算符有误")

