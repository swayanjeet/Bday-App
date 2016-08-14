from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Event
from django.contrib.auth.models import User
from django.core import serializers
import urllib2,json
from django.shortcuts import redirect,render
from bday_user.models import Bday_App_User
# Create your views here.
# All exceptions need to be defined ##

def create_event(request,admin_id,bday_user_id):
	Admin = User.objects.get(id=admin_id)
	Event_for = User.objects.get(id=bday_user_id)
	event = Event.objects.create(Admin=Admin,Event_for=Event_for)
	friends_ids = request.GET.getlist("friends[]")
	for id in friends_ids:
		event.Contributors.add(id)
	return HttpResponse("Successful")

def add_contributor(request,event_id,bday_user_id):
	data = {}
	event = Event.objects.get(id=event_id)
	user = User.objects.get(id=bday_user_id)
	#try :
	Contributor = event.Contributors.filter(id=bday_user_id)
	if Contributor.count() is 0:
		event.Contributors.add(user)
		data['response'] = 'OK'
	else : 
		data['response'] = 'NOPE'		
	#except event.Contributor.DoesNotExist :		
	return HttpResponse(json.dumps(data), content_type = 'application/json; charset=utf8')

def event_details(request,event_id):
	'''data = {}
	try :
		event = Event.objects.get(id=event_id)
		data['response'] = 'OK'
		data['details'] ={}
		data['details']['id'] = event_id
		data['details']['Admin'] = event.Admin.id
		data['details']['For'] = event.Event_for.id
		if event.Contributors.all().count()>0:
			data['details']['Contributors'] = event.Contributors.all().values()
		else :
			data['details']['Contributors'] = 0
	except Event.DoesNotExist :
		data['response'] = 'NOPE'								
	return HttpResponse(json.dumps(data), content_type = 'application/json; charset=utf8')'''
	event = Event.objects.get(id=event_id)
	Contributors = event.Contributors.all().values()
	for Contributor in Contributors:
		Contributor['profile'] = Bday_App_User.objects.get(user_id=Contributor['id'])
	user_id = request.session['user_id']
	event_id = event.id
	event_Admin = event.Admin.id
	event_Admin_profile = Bday_App_User.objects.get(user_id=event_Admin)
	event_for_id = event.Event_for.id
	event_for_profile = Bday_App_User.objects.get(user_id=event_for_id)
	#event['Admin_profile'] = Bday_App_User.objects.get(user_id=event['Admin_id']).values_list('id','name','pic')
	return render(request,'event_details.html',{'id':event_id,'for_id':event_for_id,'for_profile':event_for_profile,'admin':event_Admin,'admin_profile':event_Admin_profile,'contributors':Contributors,'user_id':user_id},content_type='text/html')


def event_details_all(request):
	user_id = request.session['user_id']
	admin_in_events = Event.objects.filter(Admin=user_id).values()
	#return HttpResponse(admin_in_events)
	for event in admin_in_events:
		event['for_name'] = Bday_App_User.objects.get(user_id=event['Event_for_id']).name
	#return HttpResponse(admin_in_events)
	contributor_in_events = Event.objects.filter(Contributors__id=user_id)	
	return render(request,'events.html',{'admin_in_events':admin_in_events,'contributor_in_events':contributor_in_events,'user_id':request.session['user_id']},content_type='text/html')

	