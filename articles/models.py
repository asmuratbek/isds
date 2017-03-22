# coding: utf-8
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'

    title = models.CharField(max_length=255, verbose_name='Заголовок материала')

    def __unicode__(self):
        return self.title


class Articles(models.Model):
    class Meta:
        verbose_name_plural = 'Материалы'
        verbose_name = 'Материал'

    title = models.CharField(max_length=255, verbose_name='Заголовок материала')
    text = RichTextUploadingField(verbose_name='Текс материала')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение материала')
    date = models.DateTimeField(auto_now_add=True, null=True)
    article = models.ForeignKey('Category', verbose_name='Категория')

    def __unicode__(self):
        return self.title


class Sliders(models.Model):
    class Meta:
        verbose_name_plural = 'Слайдеры'
        verbose_name = 'Слайдер'

    title = models.CharField(max_length=255, verbose_name='Название слайда')
    image = models.ImageField(upload_to='images/sliders', verbose_name='Изображение слайдера')
    text = models.TextField(max_length=255, verbose_name='Текст на слайде', null=True, blank=True)
    video = models.CharField(max_length=400, verbose_name='Ссылка на видео с Youtube', null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория сладера')


class Programms(models.Model):
    class Meta:
        verbose_name_plural = 'Программы'
        verbose_name = 'Программа'

    category = models.ForeignKey('Category', verbose_name='Категория')
    text = models.TextField(verbose_name='Введите текст для каждой категории в программах')


class SocialProjects(models.Model):
    class Meta:
        verbose_name_plural = 'Социальные проекты'
        verbose_name = 'Социальный проект'
    text = models.TextField(verbose_name='Текст для социальных проектов')

class Tourism(models.Model):
    class Meta:
        verbose_name_plural = 'Устойчивый Туризм'
        verbose_name = 'Устойчивый Туризм'

    text = models.TextField(verbose_name='Текст для устойчивого туризма')


class Contacts(models.Model):
    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'

    title = models.CharField(max_length=250, verbose_name='Название', default='Редактировать контакты')
    phone = models.CharField(max_length=300, verbose_name='Телефонный номер')
    email = models.CharField(max_length=300, verbose_name='Е-mail')
    address = models.CharField(max_length=300, verbose_name='Адрес')
