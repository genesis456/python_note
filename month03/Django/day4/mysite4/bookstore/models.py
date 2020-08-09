from django.db import models

# Create your models here.

"""
在 bookstore/models.py 应用中添加两个model类
1. Book - 图书
    1. title - CharField 书名,非空,唯一
    2. pub - CharField 出版社,字符串,非空
    3. price - 图书定价,,
    4. market_price - 图书零售价
2. Author - 作者
    1. name - CharField 姓名,非空
    2. age - IntegerField, 年龄,非空，缺省值为1
    3. email - EmailField, 邮箱,允许为空"""
#用一个类表示一个表
class Book(models.Model):
    #添加字段
    title = models.CharField(max_length=30,
                             db_index=True,
                             unique=True,
                             null=True,
                             verbose_name='书名')  #相当varchar(30)
    #非空null=False，默认就是非空
    pub = models.CharField(max_length=100,
                           verbose_name='出版社',
                           null=True)
    #若price在数据库创建后添加的,必须加默认值，否则迁移时会报错
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                verbose_name='定价',
                                default=99999)  #Decimal(7,2)
    market_price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                verbose_name='零售价',
                                default=99999)
    def __str__(self):
        return  "书名:" +self.title

    #- 重新定义当前模型类和数据表的一些属性信息
    class Meta:
        # - 更改模型所用的数据表的名称。(设置完成后需要立马更新同步数据库)
        # db_table = 'mybook'

        # - 给模型对象的一个易于理解的名称(单数),用于显示在/admin管理界面中
        # verbose_name = 'boooook'
        pass

class Author(models.Model):
    #添加字段
    name = models.CharField(max_length=30,
                            null=True,
                            verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄',
                              null=True,
                              default=1)

    email = models.EmailField(verbose_name='邮箱',
                              default='xxx@yy.zzz')

    def __str__(self):
        return "作者："+ self.name

    class Meta:
        db_table = 'myauthor'


class Wife(models.Model):
    name = models.CharField(max_length=30,
                            verbose_name='姓名')

    author = models.OneToOneField(Author)