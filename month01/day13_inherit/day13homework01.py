# day13 作业
# 1. 三合一
# 2. 根据需求，画出当前练习设计图.
# 3. 设计员工管理器框架

# 5. (扩展)画出天龙八部3D手游技能系统框架图。
# 6. 穷尽一切手段，在互联网中搜索"继承多态"的相关资料.
#    并结合课堂所讲(理论/代码)，总结为面向对象答辩的内容.

"""
    定义员工管理器
        1.管理所有员工
        2. 计算所有员工工资

    员工：
        程序员：底薪 + 项目分红
        销售：底薪 + 销售额 * 0.05
        软件测试...
        ...

    要求：增加新岗位，员工管理器不变.
"""
class EmployeeManager:
    """
    员工管理器
    """
    def __init__(self):
        self.__employ = []
    def add_employ(self,employ):
        """
        添加员工至私有列表
        :param employ: 传入的员工
        """
        if isinstance(employ,Employee):
            self.__employ.append(employ)
        else:
            raise ValueError()

    def Total_Employee_Salary(self):
        """
        计算所有员工工资
        :return: 总工资
        """
        total_salary = 0
        # 调用是抽象的员工类
        # 执行是具体的员工(程序员/销售..)
        for item in self.__employ:
            total_salary += item.salary()
        return total_salary

class Employee:
    """
    员工（父类）
    """
    def __init__(self,base_pay):
        self.base_pay = base_pay
    def salary(self):
        return self.base_pay

class Programmer(Employee):
    """
    程序员
    """
    def __init__(self,base_pay, project_bonus):
        # return self.base_salary + self.bonus
        # 扩展重写
        super().__init__(base_pay)   #共用的直接调用父类的
        self.project_bonus = project_bonus

    def salary(self):
        return self.base_pay + self.project_bonus

class Market(Employee):
    """
    销售
    """
    def __init__(self,base_pay,sale):
        super().__init__(base_pay)
        self.sale = sale
    def salary(self):
        return self.base_pay + self.sale * 0.05


c0 = Programmer(4000,3000)
r1 = Market(2000,500)
manager = EmployeeManager()
manager.add_employ(c0)
manager.add_employ(r1)
re = manager.Total_Employee_Salary()
print(re)

#成功的独立完成一个面向对象题（虽然老师讲几个基本一样的，但能自己想通做出来真的不错了．继续加油！）



class EmployeeManager:
    def __init__(self):
        self.__employees = []

    def add_employee(self, emp):
        self.__employees.append(emp)

    def get_total_saraly(self):
        total_saraly = 0
        for item in self.__employees:
            # 调用是抽象的员工类
            # 执行是具体的员工(程序员/销售..)
            total_saraly += item.calculate_salary()
        return total_saraly


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

# ---------------------------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        # 扩展重写
        return super().calculate_salary()+ self.bonus


class Salesmen(Employee):
    def __init__(self, base_salary, sale_value):
        super().__init__(base_salary)
        self.sale_value = sale_value

    def calculate_salary(self):
        return self.base_salary + self.sale_value * 0.05


# 测试
manager = EmployeeManager()
manager.add_employee(Programmer(200000,500))
manager.add_employee(Salesmen(2000,1000))
print(manager.get_total_saraly())


