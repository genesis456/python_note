"""

    2048控制台界面

"""

from bll import GameCoreController

from model import DirectionModel

import os  #访问操作系统的模块



class GameConsoleView:

    def __init__(self):

        self.__controller = GameCoreController()

    def main(self):

        self.__Start()

        self.__update()

    def __Start(self):

        # 产生两个数字

        self.__controller.generate_new_number()

        self.__controller.generate_new_number()

        # 绘制界面

        self.__draw_map()

    def __draw_map(self):

        # 清空控制台

        os.system("clear")   #操作系统命令clear，清空

        for row in self.__controller.map:

            for col in row:

                print(col,end= " ")

            print()

    def __update(self):

        # 循环

        while True:

            # 判断玩家的输入 --> 移动地图

            self.__move_map_for_input()

            # 产生新数字

            self.__controller.generate_new_number()

            # 绘制界面

            self.__draw_map()

            # 游戏结束判断 --> 提示

            if self.__controller.is_game_over():

                print("游戏结束")

                break

    def __move_map_for_input(self):

        dir = input("请输入方向(wsad)：")

        dict_dir = {

            "w":DirectionModel.UP,

            "W":DirectionModel.UP,

            "s":DirectionModel.DOWN,

            "S":DirectionModel.DOWN,

            "a":DirectionModel.LEFT,

            "A":DirectionModel.LEFT,

            "d":DirectionModel.RIGHT,

            "D":DirectionModel.RIGHT,



        }

        if dir in dict_dir:

            self.__controller.move(dict_dir[dir])



# ---------------测试代码----------------

# if __name__ == "__main__":
#
#     view = GameConsoleView()
#
#     view.main()