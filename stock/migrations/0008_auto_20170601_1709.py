# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 17:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20170601_0340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Historial_Price',
            new_name='Historical_Price',
        ),
    ]
