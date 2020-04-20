class Vector2:
    """
        二维向量
        可以表示位置/方向
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 静态方法:表示左边方向
    @staticmethod
    def left():
        return Vector2(0, -1)
    @staticmethod
    # 静态方法:表示右边方向
    def right():
        return Vector2(0, 1)

    @staticmethod   #向上
    def up():
        return Vector2(-1,0)

    @staticmethod   #向下
    def down():
        return Vector2(1,0)




    def print_result(self):  #行为成员
        pos01.x += l01.x
        pos01.y += l01.y
        print(pos01.x, pos01.y)

class DoubleListHelper:
        # 在二维列表中获取指定位置，指定方向，指定数量的元素.
        # 例如：list01　"10"　右边　３ --> "11", "12", "13"
        # 例如：list01　Vector2(1, 0)　Vector2.right()　３ --> "11", "12", "13"
        @staticmethod
        def get_elements(target, vect_pos, vect_dir, count):
            """
                在二维列表中获取指定位置，指定方向，指定数量的元素.
            :param target: 二维列表
            :param vect_pos: 指定位置
            :param vect_dir: 指定方向
            :param count: 指定数量
            :return: 列表
            """
            list_result = []
            for i in range(count):
                vect_pos.x += vect_dir.x
                vect_pos.y += vect_dir.y
                element = target[vect_pos.x][vect_pos.y]
                list_result.append(element)
            return list_result