from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from distrib_api import views
from rest_framework.authtoken import views as restview

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/token/', restview.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('distrib_api.urls')),
    url(r'^', include('webui.urls')),
]