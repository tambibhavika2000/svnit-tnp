# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0011_auto_20170214_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationdetail',
            name='hsc_board_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='educationdetail',
            name='ssc_board_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
