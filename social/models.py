# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class SocialLinks(models.Model):
    title = models.CharField(max_length=300, default='Редактировать социальные сети')
    f_link = models.CharField(max_length=300, verbose_name='facebook')
    t_link = models.CharField(max_length=300, verbose_name='twitter')
    i_link = models.CharField(max_length=300, verbose_name='instagramm')
    y_link = models.CharField(max_length=300, verbose_name='youtube')

    class Meta():
        verbose_name_plural = 'Социальные сети'
        verbose_name = 'Социальная сеть'

    def __unicode__(self):
        return self.title
