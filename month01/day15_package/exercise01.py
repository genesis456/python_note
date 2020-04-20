"""
    模块内置方法time练习1：定义函数，根据年月日，返回星期数。
    0 "星期一"
    1 "星期二"
    2 "星期三"
     ...
     思路：年月日 --> 时间元组
          时间元组 --> 星期
          星期 --> 格式
"""
import time

def get_week(year,month,day):
    """
    获取星期数
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 星期几的字符串
    """
    #str  --> 　时间元组　　strptime（*，*）前面一个是传入来的字符串，后面一个是变为元组的格式
    time_tuple = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")#构建一个字符串，格式来于%Y/%m/%d
    dict_weeks = {
    0 : "星期一",
    1 : "星期二",
    2 : "星期三",
    3 : "星期四",
    4 : "星期五",
    5 : "星期六",
    6 : "星期日"
    }
    return dict_weeks[time_tuple[6]]

re = get_week(2019,11,26)
print(re)


