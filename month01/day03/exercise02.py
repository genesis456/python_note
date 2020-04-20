"""
   作者：周乐
   日期：７／０７／２０１９
 练习：
 在控制台中，录入一个商品单价。
 在录入一个数量
 最后获取金额，    计算应该找回多少钱。
新增功能：当钱不够时，提示"金额不足",
　　　　钱够时，提示"应找回"
　最后,　调试程序

"""
unit_price = float(input("请输入商品单价："))

number = float(input("请输入数量："))

money = float(input("已收钱："))

result =money -  unit_price * number

if result >= 0:
    print("应找回",result)

else:
    print("金额不足")

# print("应找回",result) if result >= 0 else  print("金额不足")