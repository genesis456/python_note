"""
 练习:在控制台中循环输入字符串,如果输入空则停止。
     最后打印所有内容（拼接后的字符串）
"""

list01 = []
while True:

    str_value = input("请输入：")
    if str_value == "":
        break
    list01.append(str_value)
result = "*".join(list01)
print(result)
