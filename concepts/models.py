# coding=utf-8
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.

class MainConcepts(models.Model):
    class Meta:
        verbose_name_plural = 'Основные концепции'
        verbose_name = 'Концепция'

    title = models.CharField(max_length=255, default='Редактировать текст Основных концепций')
    bio = RichTextUploadingField(verbose_name='Биокультурное разнообразие')
    bio_image = models.ImageField(upload_to='images/main', verbose_name='Изображение для изменения биокультурное разнообразие - 790x780p')
    climate_image = models.ImageField(upload_to='images/main', verbose_name='Изображение для изменение климата - 790x780px')
    climate = RichTextUploadingField(verbose_name='Текст для именение климата')
    development_image = models.ImageField(upload_to='images/main', verbose_name='Изображение для устойчивого развития - 790x780px')
    development = RichTextUploadingField(verbose_name='Текст для утойчивого развития')
    slow_food_image = models.ImageField(upload_to='images/concepts', verbose_name='Изображение для Slow food - 790x780px')
    slow_food_text = RichTextUploadingField(verbose_name='Текст для Slow Food')

