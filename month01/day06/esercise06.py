"""
    字典练习1:在控制台中循环录入商品信息(名称,单价).
    　　　如果名称输入空字符,则停止录入.
         将所有信息逐行打印出来.
"""


dict01 = {}
while True:
    name = input("请输入名称：")
    if name == "":
        break
    unit_price = int(input("请输入单价："))
    dict01[name] = unit_price  #键和值都存入字典

for key,value in dict01.items():  #键和值都取出来
    print("%s的商品单价是%d" % (key, value))
