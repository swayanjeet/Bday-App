from django.shortcuts import render
from  django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect,render
import urllib2,json
from .models import Bday_App_User
from datetime import datetime
from django.core import serializers
from itertools import chain

def index(request):
	return render(request,'index.html',{},content_type='text/html')

def login(request):
    #social_user = request.user.social_auth.filter(provider='facebook').first()
    #response = urllib2.urlopen('https://graph.facebook.com/v2.6/me/friends?fields=installed&access_token='+social_user.extra_data['access_token'])
    #return HttpResponse("Hello "+str(social_user.extra_data['access_token']))
    #data = json.load(response.read())
    #for i in range(0,len(data)):
    if request.user.is_authenticated():
    	request.session['user_id'] = request.user.id
    	return redirect('home')
    else:
    	return HttpResponse("Done")
 
def render_home_screen(request):
	user_id = request.session['user_id']
	friends = Bday_App_User.objects.get(user_id=user_id).friends
	now = datetime.now()
	current_day = friends.filter(date_of_birth__month = 8, date_of_birth__day = 8)
	current_month = friends.filter(date_of_birth__month = 5, date_of_birth__day__gt=7)
	rest_1 = friends.filter(date_of_birth__month__gt = 5) ## First keep all the dates below it
	rest_2 = friends.filter(date_of_birth__month__gte=1,date_of_birth__month__lt=5)
	rest = list(chain(rest_1, rest_2))
	data = {}
	'''if current_day.count()>0:
		data['current_day'] = serializers.serialize('json', current_day, fields=('name','age','pic'))
	else:
		data['current_day'] = 'none'
	if current_month.count()>0:
		data['current_month'] = serializers.serialize('json', current_month, fields=('name','age','pic'))
	else:
		data['current_month'] = 'none'
	if rest_1.count() >0 or rest_2.count() > 0:
		data['rest'] = serializers.serialize('json', rest, fields=('name','age','pic'))
	else: 
		data['rest'] = 'none'''
	#return HttpResponse(json.dumps(data), content_type = 'application/json; charset=utf8')
	return render(request,'home.html',{'current_day':current_day,'user_id':request.session['user_id']},content_type='text/html')

def get_friend_list(request,user_id,for_user_id):
	friends = Bday_App_User.objects.get(user_id=user_id).friends.exclude(user=for_user_id)
	data={}
	data['friends'] = serializers.serialize('json',friends,fields=('name','user'))
	return HttpResponse(data['friends'],content_type='application/json; charset=utf8')

# Create your views her
