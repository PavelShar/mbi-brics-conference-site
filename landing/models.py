# coding: utf-8
from __future__ import unicode_literals

from django import forms
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from multiselectfield import MultiSelectField

from .helpers import *

ORGANIZERS_CHOICES = (
    ('org', 'Organising Committie'),
    ('prog', 'Programme Committie'),
)


@python_2_unicode_compatible
class BaseInfo(models.Model):
    event_type = models.CharField('Type', max_length=255)
    event_title = models.CharField('Title', max_length=255)
    event_date = models.CharField('Date', max_length=255)
    event_place = models.CharField('Place', max_length=255)
    language = models.CharField('Working language', max_length=255)

    class Meta:
        verbose_name = 'Base information'
        verbose_name_plural = 'Base information'

    def __str__(self):
        return self.event_type + " - " + self.event_title


@python_2_unicode_compatible
class Areas(models.Model):
    area_title = models.CharField('Area title', max_length=255)

    class Meta:
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.area_title


@python_2_unicode_compatible
class Speakers(models.Model):
    name = models.CharField('Name', max_length=255)
    university = models.CharField('University', max_length=255)
    description = models.TextField('Description')
    url = models.URLField('Link')
    photo = models.ImageField('Photo', upload_to=RandomFileName('speakers'))

    class Meta:
        verbose_name_plural = 'Speakers'

    def __str__(self):
        return self.name + " - " + self.university


@python_2_unicode_compatible
class TopicAreas(models.Model):
    title = models.CharField('Topic title', max_length=255)

    class Meta:
        verbose_name = 'Topic Area'
        verbose_name_plural = 'Topic Areas'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ImportantDates(models.Model):
    title = models.CharField('Title', max_length=255)
    since = models.CharField('Since', max_length=255, blank=True)
    till = models.CharField('Till', max_length=255, blank=True)
    description = models.TextField('Description', blank=True)
    svg = models.TextField('Icon')

    class Meta:
        verbose_name = 'Important Date'
        verbose_name_plural = 'Important Dates'

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Footer(models.Model):
    left_text = models.TextField('Left Text')
    phone = models.CharField('Phone', max_length=255)
    email = models.CharField('Email', max_length=255)
    site = models.URLField('Site')
    address_text = models.CharField('Address Text', max_length=255)
    address_link = models.CharField('Address Link', max_length=255)

    class Meta:
        verbose_name_plural = 'Footer'

    def __str__(self):
        return 'Footer'



@python_2_unicode_compatible
class Organizers(models.Model):

    name = models.CharField('Name', max_length=255)
    university = models.CharField(max_length=255)
    url = models.URLField()
    photo = models.ImageField(upload_to=RandomFileName('ogranizers'))
    committie = MultiSelectField(choices=ORGANIZERS_CHOICES, blank=True)

    class Meta:
        verbose_name_plural = 'Organizers'
        verbose_name = 'Organizers'

    def __str__(self):
        return self.name



@python_2_unicode_compatible
class SubmissionForm(models.Model):
    enabled = models.BooleanField('Enabled', default=False)

    class Meta:
        verbose_name = 'Submission Form'
        verbose_name_plural = 'Submission Form'

    def __str__(self):
        return "Submission form"
