# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 08:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_slidermask'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='pre_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='\u0410\u043d\u043e\u043d\u0441 \u043c\u0430\u0442\u0435\u0440\u0438\u0430\u043b\u0430'),
        ),
    ]
