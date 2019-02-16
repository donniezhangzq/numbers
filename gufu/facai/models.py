# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Number(models.Model):
	attr = models.IntegerField()
	value = models.IntegerField()
