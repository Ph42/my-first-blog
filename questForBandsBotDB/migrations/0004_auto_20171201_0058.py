# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questForBandsBotDB', '0003_auto_20171110_0455'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state_of_member',
            old_name='description',
            new_name='descript',
        ),
        migrations.RenameField(
            model_name='state_of_team',
            old_name='description',
            new_name='descript',
        ),
        migrations.RenameField(
            model_name='state_of_team_member',
            old_name='description',
            new_name='descript',
        ),
        migrations.AddField(
            model_name='member',
            name='registered_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='member',
            name='telegram_user_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='member',
            name='telegram_user_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='member',
            name='user_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='team',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='team',
            name='descript',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
