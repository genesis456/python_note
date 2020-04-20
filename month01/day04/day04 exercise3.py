"""
作者：周乐
日期：10/09/2019
    在控制台中录入一个字符串，判断是否为回文．
  判断规则:正向与反向相同．
  　　　上海自来水来自海上

"""
palindrome = input("请输入一段文字：")
print("是回文")if palindrome[:] == palindrome[::-1]else print("不是回文")




