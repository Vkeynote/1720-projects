from __future__ import unicode_literals

from django.db import models

class Track(models.Model):
	title = models.CharField(max_length = 20)
	description = models.TextField(max_length = 1000)

	def __str__(self):
		return self.title

class Speaker(models.Model):
	name = models.CharField(max_length = 40)
	bio = models.TextField(max_length = 1000)

	def __str__(self):
		return self.name

class Session(models.Model):
	title = models.CharField(max_length = 20)
	abstract = models.TextField(max_length = 2000)
	speaker = models.ForeignKey(Speaker)
	track = models.ForeignKey(Track)

	def __str__(self):
		return self.title
	
		
