
class StudentManagerController:
    """
    学生管理控制器，负责业务逻辑处理
    """

    __init_id = 1000   #类变量，表示初始编号（可以被所有对象所共享）,加两下划线表示外部不能用
    def __init__(self):      #由于学生列表是由内部的决定的，而不是由外部执行者决定
        self.__stu_list = []    #数据：学生列表


    @property
    def stu_list(self):     #获取列表也可以用行为成员，但属性更方便
        """
        学生列表
        :return: 存储学生对象的列表
         """
        return self.__stu_list

    def add_student(self, stu_info):     #将学生信息添加到列表中
        """
        添加学生信息
        """

        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self): #只能内部修改，要加双下划线
        """

        编号每次加１
        :return:加好的结果
        """
        StudentManagerController.__init_id += 1  # 上面是类变量（要用类来点info_id）
        return StudentManagerController.__init_id  # 将加１的结果赋给stu_info.id

    def remove_student(self,id):
        """
        根据ｉd移除学生信息
        :param id: 　学生id编号
        :return: 确认信息
        """
        for item in self.__stu_list:  #列表要用对象self点列表
            if item.id == id:
                self.__stu_list.remove(item)  #不能用del，因为不能完全删除元素．要用列表加ｒｅｍｏｖｅ
                return True
        return False

    def update_student(self,stu_info):
        """
        根据id修改学生信息
        :param stu_info: 外部要修改的编号
        :return: 确认信息
        """
        #根据stu_info修改其他信息
        for item in self.__stu_list:
            if item.id == stu_info.id:  #根据id修改元素，如果外部要改的元素ｉd和列表中的id相同，则修改那个
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
        按学生成绩升序排列
        """
        for r in range(len(self.__stu_list)-1):
            for c in range(r+1,len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r],self.__stu_list[c] = self.__stu_list[c],self.__stu_list[r]