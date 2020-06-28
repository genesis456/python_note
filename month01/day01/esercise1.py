"""
　　..汇率转换器
"""
# 获取数据
str_usd = input("请输入美元金额：")
#逻辑处理
result = int(str_usd) * 6.9
# 显示结果
print(result)

#程序是改出来的
#英文不好用有道
#一行代码往往是从右向左写的


price = float(input("请输入商品单价："))
number = float(input("请输入数量："))
money = float(input("收钱："))

result = money - number * price

print("应找回",result)


jin = int(input("请输入两:"))

result = jin // 16

number = jin % 16

print(result,"斤",number,"两")


distanint = int(input("请输入距离："))
time = int(input("请输入时间："))
inital_velocity = int(input("请输入初速度："))
accelerated_speed = (distanint - inital_velocity *  time )

print("加速度是：",accelerated_speed)

print(1<5)
