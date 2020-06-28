"""
函数练习1：定义计算四位整数，每位相加和的函数，
测试："1234"   "5428"
"""
# str_integer = int(input("请输入四位整数："))
# #个位
# result = str_integer % 10
# #累加
# result += str_integer // 10 % 10   #十位
# result += str_integer // 100 % 10   #百位
# result += str_integer //1000       #千位
#
#
# print("结果为:",result)


def each_add_sum(str_integer):    #函数名称一定要写得通俗易懂
    """
                                        ＃函数一定要写上注释，一定！
    :param str_integer: 计算整数的每位相加和
    :return:  　相加和
    """
    # 个位
    result = str_integer % 10
    # 累加
    result += str_integer // 10 % 10  # 十位
    result += str_integer // 100 % 10  # 百位
    result += str_integer // 1000

    return result

# 测试：
re = each_add_sum(1234)
print(re)
re = each_add_sum(5628)
print(re)