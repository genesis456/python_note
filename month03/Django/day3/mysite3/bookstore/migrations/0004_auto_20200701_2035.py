# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-07-01 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20200701_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='零售价'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(max_length=100, null=True, verbose_name='出版社'),
        ),
    ]
