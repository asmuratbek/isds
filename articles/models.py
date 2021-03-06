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
    pre_text = RichTextUploadingField(verbose_name='Анонс материала', null=True, blank=True)
    text = RichTextUploadingField(verbose_name='Текс материала')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение материала - 1920x500px')
    date = models.DateTimeField(auto_now_add=True, null=True)
    article = models.ForeignKey('Category', verbose_name='Категория')

    def __unicode__(self):
        return self.title


class Sliders(models.Model):
    class Meta:
        verbose_name_plural = 'Слайдеры'
        verbose_name = 'Слайдер'

    title = models.CharField(max_length=255, verbose_name='Название слайда')
    image = models.ImageField(upload_to='images/sliders', verbose_name='Изображение слайдера - 1920x660px')
    text = models.TextField(max_length=255, verbose_name='Текст на слайде', null=True, blank=True)
    video = models.CharField(max_length=400, verbose_name='Ссылка на видео с Youtube', null=True, blank=True)
    category = models.ForeignKey('Category', verbose_name='Категория сладера')


class Programms(models.Model):
    class Meta:
        verbose_name_plural = 'Программы'
        verbose_name = 'Программа'

    category = models.ForeignKey('Category', verbose_name='Категория')
    text = RichTextUploadingField(verbose_name='Введите текст для каждой категории в программах')

    def text_html(self):
        return self.text

    text_html.short_description = 'Content'
    text_html.allow_tags = True

    def __unicode__(self):
        return self.text


class SocialProjects(models.Model):
    class Meta:
        verbose_name_plural = 'Социальные предпринимательство'
        verbose_name = 'Социальные предпринимательство'

    text = RichTextUploadingField(verbose_name='Текст для социальных проектов')

    def text_html(self):
        return self.text

    text_html.short_description = 'Content'
    text_html.allow_tags = True

    def __unicode__(self):
        return self.text


class Tourism(models.Model):
    class Meta:
        verbose_name_plural = 'Устойчивый Туризм'
        verbose_name = 'Устойчивый Туризм'

    image = models.ImageField(upload_to='images/tourism',
                              verbose_name='Изображение для блока устойчивый туризм - 790x780px')
    text = RichTextUploadingField(verbose_name='Текст для устойчивого туризма')

    def text_html(self):
        return self.text

    text_html.short_description = 'Content'
    text_html.allow_tags = True

    def __unicode__(self):
        return self.text


class LocalLead(models.Model):
    class Meta:
        verbose_name_plural = 'Местные инициативы'
        verbose_name = "Местная инициатива"

    text = RichTextUploadingField(verbose_name='Текст для местных инициатив')

    def text_html(self):
        return self.text

    text_html.short_description = 'Content'
    text_html.allow_tags = True

    def __unicode__(self):
        return self.text


class ExpirienceChange(models.Model):
    class Meta:
        verbose_name_plural = 'Обмен опытом'
        verbose_name = 'Обмен опытом'

    text = RichTextUploadingField(verbose_name='Текст для обмена опытом')

    def text_html(self):
        return self.text

    text_html.short_description = 'Content'
    text_html.allow_tags = True

    def __unicode__(self):
        return self.text


class Contacts(models.Model):
    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакты'

    title = models.CharField(max_length=250, verbose_name='Название', default='Редактировать контакты')
    phone = models.CharField(max_length=300, verbose_name='Телефонный номер')
    email = models.CharField(max_length=300, verbose_name='Е-mail')
    address = models.CharField(max_length=300, verbose_name='Адрес')


class Publications(models.Model):
    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'

    title = models.CharField(max_length=250, verbose_name='Название')
    image = models.ImageField(upload_to='images/publication', verbose_name='Изображение для публикации - 200x200px',
                              default='1')
    text = models.CharField(max_length=300, verbose_name='Текст публикаци')
    date = models.DateTimeField(auto_now_add=True, null=True)


class Logo(models.Model):
    class Meta:
        verbose_name_plural = 'Логотипы'
        verbose_name = 'Логотип'

    title = models.CharField(max_length=255, verbose_name='Название', default='Редактировать логотипы')
    image = models.ImageField(upload_to='images/logo', verbose_name='Изображение для лого - 241x109px')


class SliderMask(models.Model):
    class Meta:
        verbose_name_plural = 'Маски слайдера'
        verbose_name = 'Маска слайдера'

    title = models.CharField(max_length=255, verbose_name='Название', default='Редактировать маски')
    image = models.ImageField(upload_to='images/slider_masks', verbose_name='Изображение для маски - 550x485px')
