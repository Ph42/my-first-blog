# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questForBandsBotDB', '0004_auto_20171201_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='id_state',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='questForBandsBotDB.state_of_team'),
        ),
    ]