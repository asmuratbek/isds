# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-15 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20170314_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/slider', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u043e\u0432')),
            ],
            options={
                'verbose_name': '\u041c\u0435\u0434\u0438\u0430',
                'verbose_name_plural': '\u041c\u0435\u0434\u0438\u0430',
            },
        ),
        migrations.CreateModel(
            name='Sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043b\u0430\u0439\u0434\u0430')),
                ('text', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0441\u043b\u0430\u0434\u0435\u0440\u0430')),
                ('image', models.ManyToManyField(to='articles.Media', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0438 \u0441\u043b\u0430\u0439\u0434\u0435\u0440\u043e\u0432')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440\u044b',
            },
        ),
    ]
