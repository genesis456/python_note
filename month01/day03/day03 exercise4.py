"""
作者：周乐
日期：03/09/2019
while练习1：
　在控制台中，获取一个开始值，一个结束值．
将中间的数字打印出来．
例如：开始值3　　结束值10
　　打印4　5　6　7　8　9
"""


start_values = int(input("请输入开始值："))
end_values = int(input("请输入结束值："))

while start_values < end_values-1 :  #如果不－1，就会打印出10
    start_values += 1
    print(start_values)


