# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokes', '0003_poke'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poke',
            name='total',
        ),
        migrations.AddField(
            model_name='user',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
