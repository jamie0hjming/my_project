# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-02 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainshow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=256)),
                ('category_id', models.CharField(max_length=20)),
                ('brandname', models.CharField(max_length=20)),
                ('img1', models.CharField(max_length=256)),
                ('child_id1', models.CharField(max_length=20)),
                ('product_id1', models.CharField(max_length=20)),
                ('long_name1', models.CharField(max_length=100)),
                ('price1', models.FloatField()),
                ('market_price1', models.FloatField()),
                ('img2', models.CharField(max_length=256)),
                ('child_id2', models.CharField(max_length=20)),
                ('product_id2', models.CharField(max_length=20)),
                ('long_name2', models.CharField(max_length=100)),
                ('price2', models.FloatField()),
                ('market_price2', models.FloatField()),
                ('img3', models.CharField(max_length=256)),
                ('child_id3', models.CharField(max_length=20)),
                ('product_id3', models.CharField(max_length=20)),
                ('long_name3', models.CharField(max_length=100)),
                ('price3', models.FloatField()),
                ('market_price3', models.FloatField()),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
    ]