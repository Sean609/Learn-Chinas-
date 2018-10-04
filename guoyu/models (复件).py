# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tempinfo(models.Model):
    name = models.CharField(max_length=20,verbose_name="单词")
    font = models.CharField(max_length=20,verbose_name='拼音')
    fanyi = models.TextField(max_length=40,verbose_name='翻译')
    juzi = models.TextField(max_length=100,verbose_name='句子')
    ph = models.FileField(verbose_name='awaz',upload_to = 'avatar/')

    #duyin = models.CharField(max_length=100,verbose_name='ukulux')
 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '国语'
        verbose_name_plural = verbose_name
