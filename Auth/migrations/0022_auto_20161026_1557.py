# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-26 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0021_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamlist',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teammembers',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]
