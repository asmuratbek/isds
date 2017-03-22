# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20170315_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0439 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0432 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430\u0445')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430',
                'verbose_name_plural': '\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b',
            },
        ),
        migrations.CreateModel(
            name='SocialProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0441\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0445 \u043f\u0440\u043e\u0435\u043a\u0442\u043e\u0432')),
            ],
            options={
                'verbose_name': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u0440\u043e\u0435\u043a\u0442',
                'verbose_name_plural': '\u0421\u043e\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Tourism',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0442\u0443\u0440\u0438\u0437\u043c\u0430')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u044b\u0439 \u0422\u0443\u0440\u0438\u0437\u043c',
                'verbose_name_plural': '\u0423\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u044b\u0439 \u0422\u0443\u0440\u0438\u0437\u043c',
            },
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address',
            field=models.CharField(max_length=300, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address_en',
            field=models.CharField(max_length=300, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address_kk',
            field=models.CharField(max_length=300, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='address_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441'),
        ),
    ]
