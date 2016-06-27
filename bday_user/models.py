from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Non_User(models.Model):
	age = models.PositiveSmallIntegerField()
	date_of_birth = models.DateField()
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	pic = models.URLField()
	facebook_id = models.CharField(max_length=200,blank=True)
	google_plus_id = models.CharField(max_length=200,blank=True)
	
class Bday_App_User(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	age = models.PositiveSmallIntegerField()
	date_of_birth = models.DateField()
	pic = models.URLField()
	facebook_id = models.CharField(max_length=200,blank=True)
	google_plus_id = models.CharField(max_length=200,blank=True)
	bday_app_friends = models.ManyToManyField("self")
	non_bday_app_friends = models.ManyToManyField(Non_User)
	
'''class Friends(models.Model):
	# Primary Friend Indicates first added friend
	Primary_friend =  # Always a bday app user
	friends = 
	bday_app_user = models.BooleanField()#'''