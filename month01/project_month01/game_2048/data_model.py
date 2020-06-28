"""
　数据模型
"""
class DirectionModel:
    """
        方向数据模型
        枚举　　大写是常量（不允许他人改变的）
    """
    #在整数基础上，添加一个人容易识别的标签
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Location:

    """
        位置
    """
    def __init__(self,r,c):

        self.r_index = r

        self.c_index = c