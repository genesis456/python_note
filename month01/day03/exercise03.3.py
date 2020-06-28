"""
  作者：周乐
  日期：１９／０７／２０１９
  if练习３：在控制台中分别录入４个数字
  打印最大的数字
(提示：将第一个数字记在心中，然后与第二个比较
　　如果第二

"""

number01 = float(input("请输入第一个数字："))
number02 = float(input("请输入第二个数字："))
number03 = float(input("请输入第三个数字："))
number04 = float(input("请输入第四个数字："))

max_value = number01  #假设第一个数字是最大值，依次与后面的数字进行比较．若大于假设的值就替换最大值

if max_value < number02:
    #发现最大的，则替换假设的
    max_value = number02

if max_value < number03:
    max_value = number03

if max_value < number04:
    max_value = number04

print("最大的数字是：",max_value)



"""
错误实例
   这个不能用嵌套，如果ｉｆ判断错误就不会执行嵌套里的
"""
# if max_value < number02:
#     #发现最大的，则替换假设的
#     max_value = number02
#
#     if max_value < number03:
#         max_value = number03
#
#         if max_value < number04:
#             max_value = number04
#
# print("最大的数字是：",max_value)


