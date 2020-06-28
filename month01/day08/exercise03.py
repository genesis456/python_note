"""
函数练习2：
定义根据两，计算几斤零几两的函数
"""
# weight_liang = int(input("请输入两："))
#
# jin = weight_liang // 16     #用／／取得整数位
#
# liang = weight_liang % 16    #用％取得小数位
#
# print(str(jin)+"斤零"+str(liang)+"两")  #全部转化为字符串才能合并


def few_jin_liang(weight_liang):
    """
    根据两计算几斤零几两
    :return:  元组： （斤，两）
    """
    jin = weight_liang // 16
    liang = weight_liang % 16
    return (jin,liang)


result = few_jin_liang(145)
print(str(result[0])+"斤零"+str(result[1])+"两")