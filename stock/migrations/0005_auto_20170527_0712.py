# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-27 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20170527_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='COM_StockCode',
            field=models.CharField(max_length=30),
        ),
    ]