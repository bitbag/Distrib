from django.conf.urls import patterns, url
from distrib_api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'group', views.GroupViewSet)
router.register(r'ipv4', views.Ipv4AddressViewSet)
router.register(r'network', views.Ipv4NetworkViewSet)
router.register(r'mission', views.MissionViewSet)
router.register(r'sub_mission', views.Sub_missionViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'playbook', views.PlaybookViewSet)
router.register(r'play_type', views.Play_typeViewSet)

urlpatterns = router.urls
