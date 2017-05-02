# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 08:39
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0006_auto_20170502_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainconcepts',
            name='bio',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='bio_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='bio_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='bio_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0411\u0438\u043e\u043a\u0443\u043b\u044c\u0442\u0443\u0440\u043d\u043e\u0435 \u0440\u0430\u0437\u043d\u043e\u043e\u0431\u0440\u0430\u0437\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='climate',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='climate_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='climate_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='climate_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0438\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u043c\u0430\u0442\u0430'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='development',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='development_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='development_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='development_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f \u0443\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0433\u043e \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='slow_food_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='slow_food_text_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='slow_food_text_kk',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food'),
        ),
        migrations.AlterField(
            model_name='mainconcepts',
            name='slow_food_text_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0434\u043b\u044f Slow Food'),
        ),
    ]
