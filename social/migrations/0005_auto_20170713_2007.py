# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 14:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20170323_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sociallinks',
            name='i_link',
        ),
        migrations.RemoveField(
            model_name='sociallinks',
            name='t_link',
        ),
    ]