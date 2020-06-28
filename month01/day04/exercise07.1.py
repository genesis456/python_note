"""
作者：周乐
日期：08/09/2019
    索引和切片练习:在控制台中获取一个字符串
打印第一个字符
打印最后一个字符
打印倒数第三个字符
打印前两个字符
倒序打印字符
如果字符串长度是奇数，则打印中间字符.

"""


str_value = input("请输入文字：")  #周乐是逗逼
print(str_value[0])
print(str_value[-1])
print(str_value[-3])
print(str_value[:2])
print(str_value[::-1])
if len(str_value) % 2 != 0:
    # print(str_value[3])
    print(str_value[len(str_value) // 2])


