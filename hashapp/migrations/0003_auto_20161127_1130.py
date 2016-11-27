# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-27 11:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hashapp', '0002_auto_20161127_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtagmodel',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='published_date',
            field=models.DateTimeField(blank=datetime.datetime(2016, 11, 27, 11, 30, 47, 901833, tzinfo=utc), null=True),
        ),
    ]
