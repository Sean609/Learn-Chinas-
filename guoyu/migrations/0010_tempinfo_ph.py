# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-11 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guoyu', '0009_auto_20180811_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempinfo',
            name='ph',
            field=models.FileField(default=0, upload_to='avatar/', verbose_name='awaz'),
            preserve_default=False,
        ),
    ]
