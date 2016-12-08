from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.
class Vector(models.Model):
  word = models.CharField(max_length=100)
  vector = models.CharField(max_length=8000)
