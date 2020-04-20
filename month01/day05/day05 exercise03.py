"""
(2) 在控制台中购买一注彩票
提示：
    "请输入第1个红球号码："
    "请输入第2个红球号码："
    "号码不在范围内"
    "号码已经重复"
    "请输入蓝球号码："
"""
list1 = []
while len(list1) < 6:
    number_red = int(input("请输入第%d个红球号码："% (len(list1)+1)))
    if number_red < 1 or number_red > 33:
        print("号码不在范围内")
    elif number_red in list1:
        print("号码已经重复")
    else:
        list1.append(number_red)

while len(list1) < 7:
    number_blue = int(input("请输入蓝球号码:"))
    if number_blue < 1 or number_blue > 16:
        print("号码不在范围内")
    else:
        list1.append(number_blue)
print("GOOD LUCK")