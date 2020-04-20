"""
作者：周乐
日期：11/09/2019
    练习２：
        在控制台中录入５个数字，
        打印最大值（不适用max）.
"""


max_value = 0  #假设一个最大值
for item in range(5):
    number = int(input("请输入第%d个数字:" % (item+1)))
    if max_value < number:
        max_value = number  #如果输入的值大于假设的，就替换假设的最大值

print(max_value)