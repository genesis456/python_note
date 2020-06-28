"""
函数练习4: 定义　判断列表中是否存在相同元素的　函数
"""
# def same_element(list01):
#     """
#
#     :param list01: 列表是否存在相同元素
#     :return: 　返回结果
#     """
#     for r in range(len(list01)-1):
#         for c in range(r+1,len(list01)):
#             if list01[r] == list01[c]:
#                 return "有重复的"
#
#     return "无重复"
# re = same_element([3, 80, 45, 5, 80, 1])
# print(re)

#建议采用bool来判断，两种可能性用Ｔrue和Ｆalse,三种用0　1　2　表示
def is_repeating(list_target):
    """

         :param list_target: 列表是否存在相同元素
         :return: 　返回结果
        """
    for r in range(0, len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] == list_target[c]:
                return True  # 有重复
    return False  # 没有重复


print(is_repeating([3, 8, 23, 5, 81, 1]))

