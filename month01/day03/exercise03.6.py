"""
  作者：周乐
  日期：２８/07/2019
  if练习6：
  在控制台中获取一个月份
   打印天数 或者提示输入有误
   １　３　５　７　８　１０　１２　--> 31天
   ４　６　９　１１　--> ３０天
   ２--> ２８天

"""
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("输入有误")
elif month == "2":
    print("有２８天")
elif month == "4" or month == "6"\
        or month == "9" or month == "11":
    print("有３０天")
else:
    print("有３１天")