# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-07 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0021_auto_20170301_0028'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='externalLink',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menu',
            name='externalURL',
            field=models.URLField(blank=True),
        ),
    ]
