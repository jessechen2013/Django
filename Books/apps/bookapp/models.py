# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Books(models.Model):
	name = models.CharField(max_length = 255)
	desc = models.TextField(default="Description")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Authors(models.Model):
	books = models.ManyToManyField(Books, related_name = "authors")
	first_name = models.CharField(max_length= 255)
	last_name = models.CharField(max_length= 255)
	email = models.CharField(max_length = 45)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)