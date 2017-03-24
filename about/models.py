# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class AboutUs(models.Model):
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=255, verbose_name='По умолчанию введите о нас')
    text = models.TextField(verbose_name='Текст для о нас')
    our_see = models.TextField(verbose_name='Текст для наше виденье')
    mission = models.TextField(verbose_name='Текст для наша миссия')
    target1_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для левого блока')
    target1_text = models.TextField(verbose_name='Текс для левого блока')
    target2_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для правого блока')
    target2_text = models.TextField(verbose_name='Текс для правого блока')
    partner1 = models.ImageField(upload_to='images/about_us', verbose_name='Лого первого партнера')
    partner2 = models.ImageField(upload_to='images/about_us', verbose_name='Лого второго партнера')

class Partnerss(models.Model):
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнер'

    title = models.CharField(max_length=255, blank=False, null=True, verbose_name='Название партнера')
    text = models.CharField(max_length=500, blank=False, null=True, verbose_name='Текст партнера')
    about = models.ForeignKey('AboutUs', verbose_name='О нас')
