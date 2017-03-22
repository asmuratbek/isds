# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Emails(models.Model):
    class Meta:
        verbose_name_plural = 'Эмейлы'
        verbose_name = 'Эмейл'

    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='Эмейл')