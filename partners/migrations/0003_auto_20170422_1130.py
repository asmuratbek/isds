# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20170330_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(upload_to='images/partners', verbose_name='\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u043f\u0430\u0440\u043d\u0435\u0440\u0430 - \u043c\u0430\u043a\u0441. \u0432\u044b\u0441\u043e\u0442\u0430 84px'),
        ),
    ]
