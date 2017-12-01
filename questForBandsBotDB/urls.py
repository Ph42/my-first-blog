from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^member_list$|^$', views.member_list, name='member_list'),
    url(r'^member_new$', views.member_new, name='member_new'),
    url(r'^member_delete/(?P<pk>)/$', views.member_delete, name='member_delete'),
   	
    url(r'^team_list$', views.team_list, name='team_list'),
    url(r'^team_new$', views.team_new, name='team_new'),


    url(r'^team_member_list$', views.team_member_list, name='team_member_list'),    
    url(r'^team_member_new$', views.team_member_new, name='team_member_new'),

       
]