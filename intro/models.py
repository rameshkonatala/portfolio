from __future__ import unicode_literals

from django.utils import timezone
from django.db import models
from datetime import timedelta,datetime


class Client(models.Model):
	name=models.CharField(max_length=30)
	mail_id=models.EmailField(max_length=30)
	comment=models.TextField()
	def __str__(self):
		return self.name
	