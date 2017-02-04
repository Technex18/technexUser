# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-03 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0018_auto_20170202_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionresponses',
            name='integerAnswer',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='questionresponses',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.options'),
        ),
        migrations.AlterField(
            model_name='quizresponses',
            name='quizTeam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.quizTeam2'),
        ),
    ]
