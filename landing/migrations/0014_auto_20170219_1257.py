# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import landing.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0013_baseinfo_background_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionGuidelines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Submission Guidelines',
                'verbose_name_plural': 'Submission Guidelines',
            },
        ),
        migrations.AlterField(
            model_name='baseinfo',
            name='background_image',
            field=models.ImageField(default='', upload_to=landing.helpers.RandomFileName('main'), verbose_name='Photo'),
        ),
    ]
