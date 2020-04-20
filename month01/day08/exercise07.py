
#定义列表升序排列的函数　


# def list_sort(list01):
#
#     for i in range(len(list01)-1):
#         for j in range(i+1,len(list01)):
#             if list01[i] > list01[j]:
#                 list01[i], list01[j] = list01[j], list01[i]
#     return list01   #调用一个列表，还得返回一个列表
#
#
# list01 = [3,80,45,5,7,1]
# re = list_sort(list01)
# print(re)

#由于上述代码传入的参数是可变对象，不需要返回方法中的变量，可以直接打印可变对象
#只是改变变量的值，变量不会变

def list_sort(list01):
    # 满足以下两个条件，就无需通过返回值传递结果。
    # 1.传入的是可变对象
    # 2.函数体修改的是传入的对象
    """
        列表升序排列的函数
    :param list01:  修改的列表　
    """

    for i in range(len(list01)-1):
        for j in range(i+1,len(list01)):
            if list01[i] > list01[j]:
                list01[i], list01[j] = list01[j], list01[i]

list01 = [3,80,45,5,7,1]
list_sort(list01)
print(list01)
