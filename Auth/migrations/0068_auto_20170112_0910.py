# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-12 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0067_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupmails',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.StartUpFair'),
        ),
    ]