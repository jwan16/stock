# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_auto_20170603_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratio',
            name='RAT_Currency',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_CurrentRatio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_DPS',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_DividendPayout',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_EPS',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_EPSGrowth',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_InventoryTurnover',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_LTDebtEquity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_NAV',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_NP',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_NPG',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_NetPM',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_OPM',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_PE',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_PreTaxPM',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_QuickRatio',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_ROC',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_ROE',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_ROTA',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_TotalDebtCapital',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_TotalDebtEquity',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='ratio',
            name='RAT_Yield',
            field=models.FloatField(null=True),
        ),
    ]
