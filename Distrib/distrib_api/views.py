from django.shortcuts import render_to_response
from distrib_api.serializers import *
from distrib_api.models import *
from rest_framework import viewsets
from rest_framework_filters import backends
import rest_framework_filters as filters
from .filters import *

class seria_viewset(viewsets.ModelViewSet):
    queryset = Service_type.objects.all()
    serializer_class = Service_type_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = ServiceTypeFilter

# class ServiceTypeFilter(filters.FilterSet):
#     ServiceName = filters.CharFilter(name='name')
#
#     class Meta:
#         model = Service_type
#         fields = ['name','alise']


class miss_viewset(viewsets.ModelViewSet):
    queryset = Miss.objects.all()
    serializer_class = Miss_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = MissFilter

class status_viewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = Status_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = StatusFilter

class log_viewset(viewsets.ModelViewSet):
    queryset = log.objects.all()
    serializer_class = log_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = LogFilter

class master_viewset(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = Master_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = MasterFilter

class playbook_viewset(viewsets.ModelViewSet):
    queryset = Playbook.objects.all()
    serializer_class = Playbook_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = PlaybookFilter

class host_viewset(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = Host_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = HostFilter

def index(request):
    strs = Miss.objects.all()
    return render_to_response('basex.html',{'sdf':strs})

def showdata(request):
    info = []
    for i in  Host.objects.all():
        info.append(i.host_ip)
    return render_to_response('basex.html',{'sdf':info})