# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from guoyu import models
from django.contrib import admin
import sys;

reload(sys);
sys.setdefaultencoding("utf8")

# Register your models here.
admin.site.register(models.Tempinfo)

