# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questForBandsBotDB', '0009_auto_20171201_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='telegram_user_id',
            field=models.IntegerField(default=-1, unique=True),
        ),
        migrations.AlterField(
            model_name='state_of_member',
            name='descript',
            field=models.CharField(choices=[('ACTIVE', 'активен'), ('DELETED', 'удалён')], default='ACTIVE', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='state_of_team_member',
            name='descript',
            field=models.CharField(choices=[('ACTIVE', 'активен'), ('DOES_NOT_RECIEVE_NOTES', 'не получает уведомления'), ('DELETED_FROM_TEAM', 'удалён из команды'), ('TEAM_DELETED', 'команда удалена')], default='ACTIVE', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
