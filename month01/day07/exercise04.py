"""
作者：周乐
日期：19/09/2019
集合练习1: 在控制台中循环录入字符串，输入空字符停止.
       打印所有不重复的文字
"""
set1 =set()
while True:
    str_input =input("请输入文字：")

    if str_input == "":
        break
    set1.add(str_input)   #放入集合中会自动将重复的丢弃

print(set1)