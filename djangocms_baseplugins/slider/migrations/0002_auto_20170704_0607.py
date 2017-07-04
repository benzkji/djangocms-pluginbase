# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-04 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='background',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='slider',
            name='color',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='slider',
            name='height',
            field=models.CharField(blank=True, default='', max_length=32, verbose_name='Height'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='layout',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
