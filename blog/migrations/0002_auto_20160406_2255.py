# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-06 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
