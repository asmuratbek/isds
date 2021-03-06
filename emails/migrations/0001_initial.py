# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u0418\u043c\u044f')),
                ('email', models.EmailField(max_length=254, verbose_name='\u042d\u043c\u0435\u0439\u043b')),
            ],
            options={
                'verbose_name': '\u042d\u043c\u0435\u0439\u043b',
                'verbose_name_plural': '\u042d\u043c\u0435\u0439\u043b\u044b',
            },
        ),
    ]
