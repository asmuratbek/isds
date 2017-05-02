# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 09:30
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_auto_20170502_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='expiriencechange',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u043f\u044b\u0442\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='expiriencechange',
            name='text_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u043f\u044b\u0442\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='expiriencechange',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043e\u0431\u043c\u0435\u043d\u0430 \u043e\u043f\u044b\u0442\u043e\u043c'),
        ),
        migrations.AddField(
            model_name='locallead',
            name='text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043c\u0435\u0441\u0442\u043d\u044b\u0445 \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432'),
        ),
        migrations.AddField(
            model_name='locallead',
            name='text_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043c\u0435\u0441\u0442\u043d\u044b\u0445 \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432'),
        ),
        migrations.AddField(
            model_name='locallead',
            name='text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u043c\u0435\u0441\u0442\u043d\u044b\u0445 \u0438\u043d\u0438\u0446\u0438\u0430\u0442\u0438\u0432'),
        ),
    ]
