from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from distrib_api import views

router = routers.DefaultRouter()
router.register(r'miss', views.miss_viewset)
router.register(r'service', views.seria_viewset)
router.register(r'status', views.status_viewset)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index/', views.index),
]