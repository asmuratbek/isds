# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class AboutUs(models.Model):
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'

    title = models.CharField(max_length=255, verbose_name='По умолчанию введите о нас')
    image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для блока о нас')
    text = models.TextField(verbose_name='Текст для о нас')
    our_see_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для нашего виденья - 790x780px')
    our_see = models.TextField(verbose_name='Текст для наше виденье')
    mission_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображения для нашей миссии - 790x780px')
    mission = models.TextField(verbose_name='Текст для наша миссия')
    target1_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для левого блока - 790x780px')
    target1_text = models.TextField(verbose_name='Текс для левого блока')
    target2_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для правого блока - 790x780px')
    target2_text = models.TextField(verbose_name='Текс для правого блока')
    partner_image = models.ImageField(upload_to='images/about_us', verbose_name='Изображение для блока партнеры - 790x780px', null=True, blank=True)
    partner1 = models.ImageField(upload_to='images/about_us', verbose_name='Лого первого партнера - 349x115px')
    partner2 = models.ImageField(upload_to='images/about_us', verbose_name='Лого второго партнера - 349x115px')


class Partnerss(models.Model):
    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнер'

    title = models.CharField(max_length=255, blank=False, null=True, verbose_name='Название партнера')
    text = models.CharField(max_length=500, blank=False, null=True, verbose_name='Текст партнера')
    about = models.ForeignKey('AboutUs', verbose_name='О нас')
