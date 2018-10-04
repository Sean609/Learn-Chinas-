# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-05 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tempinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='\u5355\u8bcd')),
                ('font', models.CharField(max_length=5, verbose_name='\u62fc\u97f3')),
                ('fanyi', models.CharField(max_length=5, verbose_name='\u7ffb\u8bd1')),
                ('juzi', models.CharField(max_length=5, verbose_name='\u53e5\u5b50')),
            ],
            options={
                'verbose_name': '\u56fd\u8bed',
                'verbose_name_plural': '\u56fd\u8bed',
            },
        ),
    ]
