# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20181102_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtypes',
            name='type_sort',
            field=models.IntegerField(),
        ),
    ]
