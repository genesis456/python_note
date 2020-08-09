from django.db import models

# Create your models here.

#用一个类表示一个表
class Book(models.Model):
    #添加字段
    title = models.CharField(max_length=30,
                             db_index=True,
                             null=True,
                             verbose_name='书名')  #相当varchar(30)
    #若price在数据库创建后添加的,必须加默认值，否则迁移时会报错
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                default=0.0,
                                verbose_name='定价')  #Decimal(7,2)
    market_price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                default=0.0,
                                verbose_name='零售价')
    pub = models.CharField(max_length=100,
                           null=True,
                           verbose_name='出版社')

class Author(models.Model):
    #添加字段
    name = models.CharField(max_length=30,
                            null=True,
                            verbose_name='姓名')
    age = models.IntegerField(null=True,
                              default=1,)

    email = models.EmailField(max_length=50,
                              default=0.0)

