# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20170316_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='text',
            field=models.CharField(max_length=500, null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430'),
        ),
    ]
