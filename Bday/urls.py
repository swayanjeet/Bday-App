"""Bday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
import social.apps.django_app.urls as social

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', social.urls),
    url(r'^$','bday_user.views.index',name='index'),
    url(r'^login/$','bday_user.views.login'),
    url(r'^home/','bday_user.views.render_home_screen',name='home'),
    url(r'^events/create-event/(?P<admin_id>\d+)/(?P<bday_user_id>\d+)','events.views.create_event',name='create_event'),
    url(r'^events/add-contributor/(?P<event_id>\d+)/(?P<bday_user_id>\d+)','events.views.add_contributor',name='add_contributor'),
    url(r'^events/event-details/(?P<event_id>\d+)','events.views.event_details',name='event_details'),
    url(r'^events/event-details/all','events.views.event_details_all',name='event_details_all'),
    url(r'^get-friends/(?P<user_id>\d+)/(?P<for_user_id>\d+)','bday_user.views.get_friend_list',name='get_friend_list'), 
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'})  
]
