# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-17 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_blogpost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(to='blogs.Tag'),
        ),
    ]