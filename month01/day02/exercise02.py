# 练习3
# 在控制台中，录入一个商品单价。25
# 在录入一个数量   2
# 最后获取金额， 60   计算应该找回多少钱。  60 -  25*2


unit_price = float(input("请输入商品单价："))

quantity = int(input("请输入数量："))
#获取金额
money = float(input("收钱："))
#需找回
change = money - unit_price * quantity
#结果
print("应该找回:",change)


