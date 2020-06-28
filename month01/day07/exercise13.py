# 函数练习1:将下列代码，定义到函数中，再调用一次.
def print_rectangle(r_count,c_count,char):  #定义函数
    """
        打印矩形
    :param r_count: 行数
    :param c_count: 列数　　　　　　＃必须要给函数加上注释（描述函数中的内容）
    :param char: 填充的字符　
    """
    for r in range(r_count):  #里面的参数可以随意改动，
        # 内层循环控制列　
        for c in range(c_count):
            print(char, end=" ")
        print()

print_rectangle(5,2,"#")  #调用函数，将形参变为实际参数（函数中需要改动的参数）
