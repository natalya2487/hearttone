# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-12 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_record_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='congenital_heart_defects',
            field=models.BooleanField(default=False, verbose_name='Congenital Heart Defects (CHD)'),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=50, null=True, verbose_name="Parent's Email"),
        ),
        migrations.AddField(
            model_name='patient',
            name='mobile_phone',
            field=models.CharField(max_length=50, null=True, verbose_name="Parent's Phone"),
        ),
        migrations.AddField(
            model_name='patient',
            name='status',
            field=models.IntegerField(choices=[(1, 'New'), (2, 'The Norm'), (3, 'Not The Norm'), (4, 'Something Strange')], default=1, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='patient',
            name='ultrasound_findings',
            field=models.ImageField(blank=True, null=True, upload_to='ultrasound', verbose_name='Ultrasound Findings'),
        ),
    ]