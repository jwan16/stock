# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20170527_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='COM_StockCode',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_COM_StockCode',
            field=models.IntegerField(max_length=30),
        ),
        migrations.AlterField(
            model_name='technical',
            name='TEC_COM_StockCode',
            field=models.IntegerField(max_length=30),
        ),
    ]
