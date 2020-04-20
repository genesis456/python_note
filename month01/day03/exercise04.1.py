"""
作者：周乐
日期：07/08/2019
练习１（exercise04所学知识）：
    在控制台中获取一个整数，
    如果是偶数为变量state赋值"偶数"，否则赋值"奇数"
"""
state = None
state = "偶数" if int(input("请输入一个整数：")) \
                % 2 == 0 else "奇数" #判断奇偶数，看是否能被２整除余０的数（求余为０的数）
print("该整数是一个:",state)




"""
继续优化（每做一个项目，先完成脑子里最熟悉的方法．然后再优化）

"""
str_integer = int(input("请输入一个整数:"))
state = "奇数" if str_integer % 2 else "偶数"
  # if str_integer % 2 表示if bool(str_integer % 2)  只要bool里面有值就执行
  #任何数除以２的最后余数不是１就是０（余数有值就是奇数，否则偶数）

print("该整数是一个:",state)