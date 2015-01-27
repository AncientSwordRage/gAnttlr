from django.conf.urls import patterns, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


api_urlpatterns = patterns('',
    url(r'^project/api/(?P<pk>[0-9]+)$', views.project_json_detail),
	url(r'^project/api/$', views.project_json_list),
	)
api_urlpatterns = format_suffix_patterns(api_urlpatterns)

urlpatterns = patterns('', 
	url(r'^(?:project)?/?$', views.project_list), # List all projects
	url(r'^project/new$', views.project_edit), # Create new project
	url(r'^project/(?P<project_id>\d+)/edit$', views.project_edit), # Edit existing project
	url(r'^project/(?P<project_id>\d+)/new$', views.task_edit), # Create new task
	url(r'^project/(?P<project_id>\d+)/(?P<task_id>\d+)/edit$', views.task_edit), # Edit existing task 
	url(r'^project/(?P<project_id>\d+)/[A-z\\-]{0,50}$', views.project_detail, name='project_detail'), #View project details

	*api_urlpatterns
	)
