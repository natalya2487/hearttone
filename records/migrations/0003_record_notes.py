# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20171102_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='notes',
            field=models.CharField(default='', max_length=256, null=True, verbose_name='Notes'),
        ),
    ]
