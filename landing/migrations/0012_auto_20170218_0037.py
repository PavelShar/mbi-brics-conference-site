# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0011_auto_20170218_0025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areas',
            options={'ordering': ('order',), 'verbose_name_plural': 'Areas'},
        ),
        migrations.AlterModelOptions(
            name='speakers',
            options={'ordering': ('order',), 'verbose_name_plural': 'Speakers'},
        ),
        migrations.AddField(
            model_name='areas',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='speakers',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
