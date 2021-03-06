# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 13:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainConcepts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442 \u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0445 \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u0439', max_length=255)),
                ('bio', models.TextField(verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435')),
                ('bio_ru', models.TextField(null=True, verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435')),
                ('bio_en', models.TextField(null=True, verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435')),
                ('bio_kk', models.TextField(null=True, verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435')),
                ('climate', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430')),
                ('climate_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430')),
                ('climate_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430')),
                ('climate_kk', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430')),
                ('development', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f')),
                ('development_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f')),
                ('development_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f')),
                ('development_kk', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f')),
                ('slow_food_imgage', models.ImageField(upload_to='images/concepts', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f Slow food')),
                ('slow_food_text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food')),
                ('slow_food_text_ru', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food')),
                ('slow_food_text_en', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food')),
                ('slow_food_text_kk', models.TextField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food')),
            ],
            options={
                'verbose_name': '\u041a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u044f',
                'verbose_name_plural': '\u041e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u0438',
            },
        ),
    ]
