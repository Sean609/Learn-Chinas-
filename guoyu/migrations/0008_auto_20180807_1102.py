# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-07 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guoyu', '0007_auto_20180807_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempinfo',
            name='ph',
            field=models.FileField(max_length=200, null=True, upload_to='uploadImages', verbose_name='awaz'),
        ),
    ]
