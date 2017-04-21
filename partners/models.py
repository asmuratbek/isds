# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Partners(models.Model):
    class Meta:
        verbose_name_plural = 'Партнеры'
        verbose_name = 'Партнер'
        ordering = ('my_order',)

    title = models.CharField(max_length=255, verbose_name='Название партнера')
    image = models.ImageField(upload_to='images/partners', verbose_name='Логотип парнера - макс. высота 84px')
    url = models.CharField(max_length=255, verbose_name='Ссылка на сайт')
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)
