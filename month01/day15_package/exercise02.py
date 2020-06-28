"""
作者：周乐
日期：26/11/2019
 模块内置方法time练习2：根据生日(年月日)，计算活了多少天。
 思路：
 年月日 --> 出生时间
 当前时间 --> 出生时间
 计算天
"""
import time

def get_day(year,month,day):
    """
    根据生日计算活了多少天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 根据总秒数返回天数
    """
    tuple_time = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")#构建一个字符串，格式来于%Y/%m/%d
    life_second = time.time() - time.mktime(tuple_time) #time.time()获取当前时间戳，然后减去出生的时间戳
    return int(life_second / 60 /60 //24) #根据总秒获取天数

print(get_day(2001,2,24))