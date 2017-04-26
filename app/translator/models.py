# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from app.converter.models import File
from choices import LANGUAGE_CHOICES
from utils import TranslateFile
import os

class Translated(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE,
							 null=False, blank=False)
	language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, null=False, blank=False)
	translated_file = models.CharField(max_length=100, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		TranslateFile(self)
		super(Translated, self).save()

	def __unicode__(self):
		return self.translated_file