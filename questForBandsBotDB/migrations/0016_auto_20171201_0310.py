# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questForBandsBotDB', '0015_auto_20171201_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
