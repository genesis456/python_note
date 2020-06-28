"""
　　将game_2048_core模块整理
"""


map = [
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]
def zero_to_end(list_merge):
    """
    零元素移到末尾
    """
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] == 0 :
            del list_merge[i]
            list_merge.append(0)

def merge_same_number(list_merge):
    """
    合并
    """
    zero_to_end(list_merge)
    for j in range(len(list_merge)-1):
        if list_merge[j] == list_merge[j+1]:
            list_merge[j] += list_merge[j+1]
            del list_merge[j+1]
            list_merge.append(0)

class Move:
    @staticmethod
    def move_left():
        """
        向左移动
        """
        for line in map:
            list_merge = line
            merge_same_number(list_merge)
    @staticmethod
    def move_right():
        """
        向右移动
        """
        for line in map:
            list_merge = line[::-1]
            merge_same_number(list_merge)
            line[::-1] = list_merge
    @staticmethod
    def move_upward():
        """
       向上移动
       利用方阵转置

        """
        square_transpose(map)
        Move.move_left()
        square_transpose(map)
    @staticmethod
    def move_down():
        """
       向下移动
       利用方阵转置
        """
        square_transpose(map)
        Move.move_right()
        square_transpose(map)

def square_transpose(list01):
    """　
    :return: 方阵转置
    """
    for c in range(1, len(list01)):
        for r in range(c, len(list01)):
            list01[r][c-1], list01[c-1][r] = list01[c-1][r], list01[r][c-1]

# print("---左移----")
# move_left()
# for item in map:
#     print(item)
#
# print("---右移----")
# move_right()
# for item in map:
#     print(item)

print("---下移----")
Move.move_down()
for item in map:
    print(item)

print("---上移----")
Move.move_upward()
for item in map:
    print(item)
