#CoreController逻辑处理
"""
    游戏逻辑控制器，负责处理游戏核心算法．
"""
from model import DirectionModel
from model import Location
import random
class GameCoreController:
    def __init__(self):
        self.__list_merge = None     #都要用的数据
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]  #不想被外部所用，私有
        self.__list_empty_location = []
    @property        #保护私有属性,拦截读写操作
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
        零元素移到末尾
        """


        for i in range(-1, -len(self.__list_merge)- 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge_same_number(self):
        """
        合并
        """
        self.__zero_to_end()
        for j in range(len(self.__list_merge) - 1):
            if self.__list_merge[j] == self.__list_merge[j + 1]:
                # 将后一个累加前一个之上
                self.__list_merge[j] += self.__list_merge[j + 1]
                # 删除后一个，并补0
                del self.__list_merge[j + 1]
                self.__list_merge.append(0)

    def __move_left(self):
        """
        向左移动
        """
        # 思想：将二维列表中每行交给merge函数进行操作
        for line in self.__map:
            self.__list_merge = line  # 将大列表中的每个小列表元素传给list_merge
            self.__merge_same_number()

    def __move_right(self):
        """
        向右移动
        """
        # 思想：将二维列表中每行（从右向左）交给merge函数进行操作
        for line in self.__map:
            self.__list_merge = line[::-1]  ######从右向左取出数据，形成新列表，
            ##########list_merge 执行完后要赋值给原来的line列表才行＃＃＃
            self.__merge_same_number()  # 第二个元素结束是4　8　0　0
            # 从右向左接收　　合并后的数据　　　0　0　8　4　
            line[::-1] = self.__list_merge

    def __move_upward(self):
        """
       向上移动
       利用方阵转置

        """
        self.square_transpose()  # （转置完向左移）
        self.__move_left()
        self.square_transpose()  # 再进行转置还原

    def __move_down(self):
        """
       向下移动
       利用方阵转置

        """
        self.square_transpose()  # （转置完向右移）
        self.__move_right()
        self.square_transpose()  # 再进行转置还原
    ##根据代码的艺术性，优化代码．（将众多的方向私有并进行封装）

    def square_transpose(self):
        """

        :return: 方阵转置
        """
        for c in range(1, len(self.__map)):
            for r in range(c, len(self.__map)):
                self.__map[r][c - 1], self.__map[c - 1][r] = self.__map[c - 1][r], self.__map[r][c - 1]

    def move(self,dir):
        """
            移动
        :param dir: 方向，　DirectionModel类型
        :return:
        """


        if dir == DirectionModel.UP:
            self.__move_upward()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()



    # def generate_new_number(self):
    #     list_empty_location = []
    #     #思路：选出所有的空白位置（行／列），再随机挑选一个
    #     for r in range(len(self.__map)):  #行0　1　2　3
    #         for c in range(len(self.__map[r])):  #列
    #             if self.__map[r][c] == 0:
    #                 list_empty_location.append((r,c))  #将0的位置存放好（而不是存0）
    #     #随机选取出一个0,产生随机数
    #     loc = random.choice(list_empty_location)
    #     if random.randint(1,10)==1:   #出现１的概率是10%(将一个4放在随机空白位置)
    #         self.__map[loc[0]][loc[1]] = 4 #将随机选取出一个0（r,c）的位置换成4
    #     else:            #90%
    #         self.__map[loc[0]][loc[1]] = 2
    ##代码凌乱，结构不清晰．．继续优化代码##

    def generate_new_number(self):
        """
         生成新数字
        :return:
        """

        #获取所有空白位置
        self.__get_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        #确定哪个空白位置（随机产生一个空白位置）
        loc = random.choice(self.__list_empty_location)
        #如果1~10产生的随机数是1（说明概率是10%），就返回4。否则不等于1的概率是90%，返回2
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2

        # 因为在该位置生成了新数字，所以该位置就不是空位置了
        self.__list_empty_location.remove(loc)

    def __get_empty_location(self):
        # 每次统计空位置，都先清空之前的数据，避免影响本次的数据
        self.__list_empty_location.clear()

        for r in range(len(self.__map)):  #行
            for c in range(len(self.__map[r])):  #列
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(Location(r,c))
                    # 产生随机数
        return self.__list_empty_location

    def is_game_over(self):

        """

            游戏是否结束

        :return:False表示游戏没有结束True表示结束

        """

        # 是否具有空位置

        if len(self.__list_empty_location) > 0:
            return False
        # # 判断横向有没有相同的元素
        # for row in range(len(self.__map)):
        #     for col in range(len(self.__map[row])-1):
        #         if self.__map[row][col] == self.__map[row][col + 1]:
        #             return False
        # # 判断竖向有没有相同的元素
        # for col in range(4):
        #     for row in range(3):
        #         if self.__map[row][col] == self.__map[row + 1][col]:
        #             return False

        # 判断横向有没有相同的元素

        for row in range(len(self.__map)): #行数

            for col in range(len(self.__map[row]) - 1): #每行中的元素纵坐标（最后一个元素不用）
                    #判断每行是否有相同的元素或者每列有相同的元素
                if self.__map[row][col] == self.__map[row][col + 1] or self.__map[col][row] == self.__map[col + 1][row]:
                    return False

        return True


#------------------------------------测试代码－－－－－--------－－－－----------
if __name__ == "__main__":

     controller = GameCoreController()
    #
    # controller.move_left()
    #
    # print(controller.map)
    #
    # controller.move_down()
    # print(controller.map)
    #
    # controller.move_right()
    # print(controller.map)

####优化代码###############
     # controller.move(DirectionModel.UP)
     # print(controller.map)

#升级功能，增加随机数###


     controller.generate_new_number()

     controller.generate_new_number()

     controller.generate_new_number()

     controller.is_game_over()

     print(controller.map)







