# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-03 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodtypes',
            name='type_id',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='goods',
            name='dealer_id',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='goods',
            name='product_id',
            field=models.IntegerField(max_length=10),
        ),
    ]
