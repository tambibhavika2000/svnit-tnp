# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0013_auto_20170217_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationdetail',
            name='college_passout_year',
            field=models.CharField(default=2017, max_length=4),
            preserve_default=False,
        ),
    ]
