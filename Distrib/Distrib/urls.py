from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from distrib_api import views
from rest_framework.authtoken import views as restview

router = routers.DefaultRouter()
router.register(r'miss', views.miss_viewset)
router.register(r'submiss', views.submiss_viewset)
# router.register(r'service', views.seria_viewset)
# router.register(r'status', views.status_viewset)
router.register(r'log', views.log_viewset)
router.register(r'master', views.masters_viewset)
router.register(r'playbook', views.playbook_viewset)
router.register(r'host', views.hosts_viewset)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api/token/', restview.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index/', views.index),
    url(r'^createmission/', views.CreateMission),
    # url(r'^rewis/', views.WriteToRedis),
    # url(r'^redis/', views.GetFromRedis),
]