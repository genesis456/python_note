"""
作者：周乐
日期：12/09/2019
　练习:英文单词翻转
 "How are you" -->"you are How"
"""

list01 = "How are you"
#先要用列表拆分来判断单词个体（组成列表）
str_temp = list01.split(" ")

#然后在将列表倒序并转换成字符串
list_result = " ".join(str_temp[::-1])
print(list_result)

