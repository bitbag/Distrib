from django.shortcuts import render_to_response
from distrib_api.serializers import *
from distrib_api.models import *
from rest_framework import viewsets

class seria_viewset(viewsets.ModelViewSet):
    queryset = Service_type.objects.all()
    serializer_class = Service_type_ser

class miss_viewset(viewsets.ModelViewSet):
    queryset = Miss.objects.all()
    serializer_class = Miss_ser

class status_viewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = Status_ser

class log_viewset(viewsets.ModelViewSet):
    queryset = log.objects.all()
    serializer_class = log_ser

class master_viewset(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = Master_ser

class playbook_viewset(viewsets.ModelViewSet):
    queryset = Playbook.objects.all()
    serializer_class = Playbook_ser

class host_viewset(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = Host_ser

def index(request):
    strs = Miss.objects.all()
    return render_to_response('basex.html',{'sdf':strs})