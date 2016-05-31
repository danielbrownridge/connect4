# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-17 01:02
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect4', '0002_game_moves'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='game',
            name='moves',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=42),
        ),
    ]