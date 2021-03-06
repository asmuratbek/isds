# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_auto_20170331_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderMask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043c\u0430\u0441\u043a\u0438', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to='images/slider_masks', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043c\u0430\u0441\u043a\u0438')),
                ('image_ru', models.ImageField(null=True, upload_to='images/slider_masks', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043c\u0430\u0441\u043a\u0438')),
                ('image_en', models.ImageField(null=True, upload_to='images/slider_masks', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043c\u0430\u0441\u043a\u0438')),
                ('image_kk', models.ImageField(null=True, upload_to='images/slider_masks', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043c\u0430\u0441\u043a\u0438')),
            ],
            options={
                'verbose_name': '\u041c\u0430\u0441\u043a\u0430 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
                'verbose_name_plural': '\u041c\u0430\u0441\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u0430',
            },
        ),
    ]
