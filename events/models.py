from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Event(models.Model):
	Admin = models.ForeignKey(User,related_name="admin",on_delete=models.CASCADE) # meaning of models.cascade
	Event_for = models.ForeignKey(User,related_name="event_for",on_delete = models.CASCADE)
	Contributors = models.ManyToManyField(User,related_name="contributor",blank=True)



 
