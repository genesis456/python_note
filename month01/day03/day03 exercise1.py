"""
作者：周乐
日期：０１／０９／２０１９
day03作业１：
    在控制台中获取月份，显示季度，或者提示月份错误．
"""
month = int(input("请输入月份："))
if month < 1 or month > 12:
    print("月份错误")
elif month <= 3:
    print("春天")
elif month <= 6 :
    print("夏天")
elif month <= 9:
    print("秋天")
else:
    print("冬天")