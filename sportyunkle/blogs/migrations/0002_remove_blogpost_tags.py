# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-17 12:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
    ]
