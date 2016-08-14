from .models import Bday_App_User
import urllib2,json
from django.http import HttpResponseRedirect,HttpResponse
from datetime import datetime
import urllib,json,requests

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        try:
            profile = Bday_App_User.objects.get(user=user)
            print "DOne"
        except Bday_App_User.DoesNotExist:
            profile = None        
        if profile is None:
            social_user = user.social_auth.filter(provider='facebook').first()
            Fb_id = social_user.extra_data['id']
            try :
                profile = Bday_App_User.objects.get(facebook_id=Fb_id)
            except Bday_App_User.DoesNotExist:
                profile = None   
            if profile is None:
                access_token = social_user.extra_data["access_token"]
                # Step 1 Obtaining Name and Facebook Id
                profile = Bday_App_User.objects.create(user=user,age=10)
                profile.profile_type='F'
                profile.facebook_id = Fb_id
                data = profile.get_profile(access_token)
                profile.available = True
                profile.name = data['name']
                profile.date_of_birth = datetime.strptime(data['birthday'], "%m/%d/%Y").date()
                profile.calculate_age()
                profile.save()
                data = profile.get_profile_pic(access_token)
                profile.pic = data['data']['url']
                profile.save()
                # Step 2 Loading all the Friends and Creating their Profile ids if not available and associating them with Profiles
                profile.update_friendlist(access_token)
            else:
                profile.user = user
                profile.available = True
                access_token = social_user.extra_data["access_token"]
                profile.update_profile(access_token)
                profile.save()
        else:
            social_user = user.social_auth.filter(provider='facebook').first()
            access_token = social_user.extra_data["access_token"]
            profile.available = True
            profile.update_profile(access_token)
            profile.save()          
    elif backend.name == 'google-oauth2':
        social = user.social_auth.filter(provider='google-oauth2').first()
        access_token = social.extra_data['access_token']
        '''data = urllib.urlencode({'access_token' : social.extra_data['access_token'], 'fields':'birthday,name'})
        print data
        response = urllib2.urlopen('https://www.googleapis.com/plus/v1/people/me',data)
        print response.read()
        response = requests.get('https://www.googleapis.com/plus/v1/people/me',params={'access_token': social.extra_data['access_token'],'fields':'birthday,image/url,displayName'})
        url,par = response.json()['image']['url'].split("?")'''
        
        '''response = requests.get('https://www.googleapis.com/plus/v1/people/me/people/visible', params = {'access_token': social.extra_data['access_token'], 'fields':'items(birthday,displayName,id,image/url)'})
        count = 0;
        data = response.json()
        print response.json()
        friend_list = data['items']
        #print data
        #if data['nextPageToken'] is not None:
        for i  in range(0,len(friend_list)):
            print friend_list[i]['displayName']
            response = requests.get('https://www.googleapis.com/plus/v1/people/'+friend_list[i]['id'],params={'access_token': social.extra_data['access_token'],'fields':'ageRange,birthday'})
            print response.json()'''

        #print response.json()
        try:
            profile = Bday_App_User.objects.get(user=user)
            profile.update_profile(access_token)
            profile.update_friendlist(access_token)
            print "DOne"
        except Bday_App_User.DoesNotExist:
            profile = None        
        if profile is None:
            social_user = user.social_auth.filter(provider='google-oauth2').first()
            response = requests.get('https://www.googleapis.com/plus/v1/people/me',params={'access_token': social.extra_data['access_token'],'fields':'id'})
            google_plus_id = response.json()['id']
            try :
                profile = Bday_App_User.objects.get(google_plus_id=google_plus_id)
            except Bday_App_User.DoesNotExist:
                profile = None   
            if profile is None:
                # Step 1 Obtaining Name and Facebook Id
                profile = Bday_App_User.objects.create(user=user,age=10,profile_type='G')
                profile.google_plus_id = google_plus_id
                profile.available = True
                profile.update_profile(access_token)
                profile.save()
                # Step 2 Loading all the Friends and Creating their Profile ids if not available and associating them with Profiles
                profile.update_friendlist(access_token)
            else:
                profile.user = user
                profile.available = True
                profile.update_profile(access_token)
                profile.update_friendlist(access_token)
                profile.save()
        else:
            profile.available = True
            profile.update_profile(access_token)
            profile.update_friendlist(access_token)
            profile.save()
        


                