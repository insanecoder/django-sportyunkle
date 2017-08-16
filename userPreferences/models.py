# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	firstName=  models.CharField(max_length=30)
	lastName=  models.CharField(max_length=30)
	email=  models.CharField(max_length=30)
	password=  models.CharField(max_length=255,unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
