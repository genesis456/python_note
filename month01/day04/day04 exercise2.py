"""
作者：周乐
日期：09/09/2019
　在控制台中获取一个整数作为边长．
　　根据边长打印矩形．
   例如：４
       ****
       *  *
       *  *
       ****

       6
       ******
       *    *
       *    *
       *    *
       *    *
       ******
"""

number = int(input("请输入边长："))  # 4　　做题如果没思路，先假设一个，然后慢慢推出来
print("*"*number)
for item in range(number-2):  #减去首位的
    print("*"+" "*(number-2)+"*")  #要先算number-2所以需加一个小括号
print("*"*number)