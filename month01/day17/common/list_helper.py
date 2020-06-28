"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item
    @staticmethod
    def find(list_skill,change):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param change: 需要查找的条件,函数类型
            函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_skill:
            if change(item):
                return item   #单个元素用return

    @staticmethod    #day17/homework中的获取元素数量方法和判断某个条件的元素是否存在的方法
    def get_count(list_target, func_duration):
        """
               通用的计算满足某个条件的元素数量方法
           :param list_target: 需要查找的列表
           :param func_duration: 需要查找的条件,函数类型
                   函数名(参数) --> bool
           :return: 满足条件元素的数量
        """
        count_value = 0
        for item in list_target:
            if func_duration(item):
                count_value += 1
        return count_value
    @staticmethod
    def is_exists(list_target, messger):  # messger替代judge01和judge02
        """
               通用的判断某个条件的元素是否存在的方法
           :param list_target: 需要查找的列表
           :param messger: 需要查找的条件,函数类型
                   函数名(参数) --> bool
           :return: bool类型，True表示存在，False表示不存在
        """
        for item in list_target:
            if messger(item):
                return True
        return False

    @staticmethod          #day18/exercise01中求和方法
    def add_sum(list_target, add_number):
        """
               通用的求和方法
           :param list_target: 需要查找的列表
           :param add_number: 需要求和的处理逻辑,函数类型
                   函数名(参数) -->int/float
           :return: 和
        """
        sum_value = 0
        for item in list_target:
            sum_value += add_number(item)
        return sum_value

    @staticmethod      #day18/exercise02中筛选方法
    def screen(list_target,screen_data):
        """
           通用的筛选方法
       :param list_target: 需要查找的列表
       :param screen_data: 需要求和的处理逻辑,函数类型
               函数名(参数) -->int/float
       :return: 生成器
        """
        for item in list_target:
            yield screen_data(item)

    @staticmethod      #day18/exercise03中获取最大最小值
    def get_max(list_target,max_data):
        """
               通用的获取最大元素的方法
           :param list_target: 需要搜索的列表
           :param max_data: 需要搜索的处理逻辑,函数类型
                   函数名(参数) -->int/float
           :return: 最大元素
        """
        max_value = list_target[0]   #假设列表第一个元素为最大的
        for i in range(1,len(list_target)):  #将后面的元素打印出来
            if max_data(list_target[i])> max_data(max_value):#将第一个元素中需要比较的数据与后面数据比较，取出最大的
                #list_target[i]和maximum用item替换
                max_value = list_target[i]
        return max_value
    @staticmethod
    def get_min(list_target,min_data):
        """
               通用的最小获取元素的方法
           :param list_target: 需要搜索的列表
           :param min_data: 需要搜索的处理逻辑,函数类型
                   函数名(参数) -->int/float
           :return: 最小元素
        """
        min_value = list_target[0]
        for i in range(1,len(list_target)):
            if min_data(list_target[i]) < min_data(min_value):
                min_value = list_target[i]
        return min_value

    @staticmethod     #day18/exercise04中升序排列方法和降序排列方法
    def ascending_order(list_target,order_value):
        """
          通用的升序排列方法
        :param list_target: 需要排序的数据
        :param order_value: 排序的逻辑
        　　　函数（参数）　－－＞　int/float..需要比较的数据
        :return:# 没有对列表内部进行修改，所以无需返回值(直接对列表进行查看)
        """
        # 取出前几个数据
        for r in range(len(list_target) - 1):  # 0 1 2
            # 与后面的进行比较
            for c in range(r + 1, len(list_target)):  # 1 2 3 4
                if order_value(list_target[r]) > order_value(list_target[c]):
                    list_target[r], list_target[c] = list_target[c], list_target[r]
    @staticmethod
    def descending_order (list_target,order_va):
        """
          通用的降序排列方法
        :param list_target: 需要排序的数据
        :param order_value: 排序的逻辑
        　　　函数（参数）　－－＞　int/float..需要比较的数据
        :return:# 没有对列表内部进行修改，所以无需返回值(直接对列表进行查看)
        """
        for i in range(len(list_target)-1):
            for j in range(i+1,len(list_target)):
                if order_va(list_target[i]) < order_va(list_target[j]):
                    list_target[i],list_target[j] = list_target[j],list_target[i]

    @staticmethod    #day18/homework中容器根据指定条件删除元素
    def delete_all(list_target,fun_delete):   #day18/homework中容器根据指定条件删除元素
        """
            根据指定条件删除元素
        :param list_target: 　需要删除的列表
        :param fun_delete: 删除条件
        ＃容器内部修改，无需返回值
        """
        # 删除要反向索引　3　2　1　0
        for i in range(len(list_target) - 1, -1, -1):
            # if list01[i].phylactic>100:
            if fun_delete(list_target[i]):
                del list_target[i]