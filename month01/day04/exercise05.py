"""
作者：周乐
日期：06/09/2019
字符串编码练习1：在控制台中，获取一个字符串，
    打印
    每个字符的编码值
"""

str_unit = input("请输文字：")

for item in str_unit:

    print(ord(item))  #每个字符的编码值


"""
作者：周乐
日期：06/09/2019
字符串编码练习2：在控制台中，重复录入一个编码值，然后打印字符
    如果输入空字符串，则退出程序
"""



while True:
    number01 = input("请输入编码值：")  #因为如果是空字符串不用加int，所以要多写一个number
    if number01 == "":
        breinputk

    number02 = int(number01)  #number02 只需将前面的number01提下来，再加上整型int.
                                #不然多做一遍，又要重新输出一次
    print(chr(number02))
