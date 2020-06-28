"""
     古代的秤一斤是16两
练习4：在控制台中获取两，计算是几斤零几两。
    显示几斤零几两
"""


#正确写法
weight_liang = int(input("请输入两："))

jin = weight_liang // 16     #用／／取得整数位

liang = weight_liang % 16    #用％取得小数位

print(str(jin)+"斤零"+str(liang)+"两")  #全部转化为字符串才能合并


