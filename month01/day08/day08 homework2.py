"""
作者：周乐
日期：26/10/2019
定义函数，计算指定范围内的素数
"""

"""
def get_prime(begin,end):
    list01 = []
    #生成指定范围内的整数
    for number in range(begin,end):
        #判断素数
         for item in range(2,number):
            if number % item == 0:
                break   #都不等于0就退出循环体
         else:#都不等于0（说明是素数，保存列表里）
            list01.append(number)
    return list01

print(get_prime(5,30))

"""
#做出基本功能后，要对代码进行质量优化（函数要做到分而治至，只干一件事）
# def get_prime(begin,end):#5  30
#     list_result = []
#     # 生成范围内的整数
#     for number in  range(begin,end):
#         # 判断素数
#        if is_prime(number):
#            list_result.append(number)
#     return list_result
#
#
# def is_prime(number):
#     for item in range(2, number):
#         if number % item == 0:
#             return
#     return True
#
#
#
# print(get_prime(5,30))

#再将代码中的循环用推导式替换，简化代码（并将函数注释写清楚，以方便同伴使用）
def is_prime(number):
    """
    判断指定的数字是否为素数
    :param
    number: 指定的整数
    :return: True
    表示是素数，False表示不是素数.
    """
    for item in range(2, number):
        if number % item == 0:
            return False
    return True

def get_prime(begin, end):  # 5  30
    """"
    获取范围内的素数
    :param
    begin: 开始值(包含)
    :param
    end: 结束值(不包含)
    :return: 所有素数的列表
    """
    return [number for number in range(begin, end) if is_prime(number)]


print(get_prime(5, 30))








