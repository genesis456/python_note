class StudentModel:
    """
    学生信息模型
    """
    def __init__(self,name="",age=0,score=0,id=0):  #默认参数从右往左写
        """
        创建学生对象
        :param name: 姓名，str
        :param age: 年龄，int
        :param score: 成绩,float
        :param id: 编号（该学生对象的唯一标识）
        """


        self.name = name
        self.age = age
        self.score = score
        self.id = id