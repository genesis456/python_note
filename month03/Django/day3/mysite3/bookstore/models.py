from django.db import models

# Create your models here.

#用一个类表示一个表
class Book(models.Model):
    #添加字段
    title = models.CharField(max_length=30)  #相当varchar(30)
    price = models.DecimalField(decimal_places=2,
                                max_digits=7)  #Decimal(7,2)
