from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import urllib2,json,requests

## issues if two persons have profiles from both the networks ###

class Bday_App_User(models.Model):
	PROFILE_TYPE_CHOICES = (('F','facebook'),('G','google')) 
	user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True,null=True)
	name = models.CharField(max_length=100,blank=True,null=True)
	age = models.PositiveSmallIntegerField(blank=True,null=True)
	date_of_birth = models.DateField(blank=True,null=True)
	pic = models.URLField(blank=True,null=True)
	facebook_id = models.CharField(max_length=200,blank=True,null=True)
	google_plus_id = models.CharField(max_length=200,blank=True,null=True)
	friends = models.ManyToManyField("self",blank=True)
	available = models.BooleanField(default=False)
	profile_type = models.CharField(max_length=2,choices=PROFILE_TYPE_CHOICES,null=True)
#non_bday_app_friends = models.ManyToManyField(Non_User)

	def calculate_age(profile): 
		now = datetime.now()
		if profile.date_of_birth.year != None:
			profile.age = now.year-profile.date_of_birth.year
			profile.save()

	def get_profile_pic(self,access_token):
		#if self.profile_type=='F':
		#if self.profile_type=='F':
		response = urllib2.urlopen('https://graph.facebook.com/v2.6/'+self.facebook_id+'/picture?type=normal&redirect=False&access_token='+access_token)
		data = json.loads(response.read())
		print data
		return data
			#respone = requests.	

	def get_profile(self,access_token):
		#if self.profile_type=='F'
		print self.facebook_id
		response = urllib2.urlopen('https://graph.facebook.com/v2.6/'+self.facebook_id+'?fields=id%2Cname%2Cbirthday&access_token='+access_token)
		data = json.loads(response.read())
		return data

	def update_profile(self,access_token):
	# Update the profile here
		if self.profile_type=='F':
			data = self.get_profile_pic(access_token)
			self.pic = data['data']['url']
			data = self.get_profile(access_token)
			self.name = data['name']
			self.date_of_birth = datetime.strptime(data['birthday'], "%m/%d/%Y").date()
			self.calculate_age()
			self.update_friendlist(access_token)
			self.save()
		elif self.profile_type=='G':
			response = requests.get('https://www.googleapis.com/plus/v1/people/'+self.google_plus_id,params={'access_token': access_token,'fields':'birthday,image/url,displayName'})
			url,par = response.json()['image']['url'].split("?")
			self.pic = url+"?sz=200"
			self.name = response.json()['displayName']
			if "birthday" in response.json():
				try :
					self.date_of_birth = datetime.strptime(response.json()['birthday'], "%Y-%m-%d").date()
					self.calculate_age()
				except ValueError:
					self.date_of_birth = None	
			#self.update_friendlist(access_token)
			self.save()	 

	def update_friendlist(self,access_token):
	# Update Friends Profile 
		if self.profile_type=='F':
			response = urllib2.urlopen('https://graph.facebook.com/v2.6/me/friends?fields=id%2Cname%2Cbirthday&access_token='+access_token)
			data = json.loads(response.read())
			data = data['data']
			for i in range(0,len(data)):
				Friend_fb_id = data[i]['id']
				Friend_bday =  datetime.strptime(data[i]['birthday'], "%m/%d/%Y").date()
				Friend_Name = data[i]['name']
				try :
					Friend_Profile = Bday_App_User.objects.get(facebook_id=Friend_fb_id)
				except Bday_App_User.DoesNotExist:
					Friend_Profile = None
		        
				if Friend_Profile is None:
					Friend_Profile = Bday_App_User.objects.create(facebook_id=Friend_fb_id,name=Friend_Name,date_of_birth=Friend_bday,age=10)
					Friend_Profile.calculate_age()
					pic_data = Friend_Profile.get_profile_pic(access_token)
					Friend_Profile.pic = pic_data['data']['url']
					Friend_Profile.friends.add(self)
					Friend_Profile.save()    
			self.save() 
		elif self.profile_type=='G':
			response = requests.get('https://www.googleapis.com/plus/v1/people/me/people/visible', params = {'access_token': access_token, 'maxResults': 5,'fields':'items(birthday,displayName,id,image/url)'})
			data = response.json()['items']
			for i in range(0,len(data)):
				Friend_google_id = data[i]['id']
				Friend_Name = data[i]['displayName']
				Friend_pic,par = data[i]['image']['url'].split("?")
				Friend_pic += "?sz=200"
				try :
					Friend_Profile = Bday_App_User.objects.get(google_plus_id=Friend_google_id)
					Friend_Profile.update_profile(access_token)
				except Bday_App_User.DoesNotExist:
					Friend_Profile = None
		        
				if Friend_Profile is None:
					Friend_Profile = Bday_App_User.objects.create(google_plus_id=Friend_google_id,name=Friend_Name,date_of_birth=None,age=10,profile_type='G')
					Friend_Profile.update_profile(access_token)
					Friend_Profile.pic = Friend_pic
					Friend_Profile.friends.add(self)
					Friend_Profile.save()
			self.save() 	

	
	