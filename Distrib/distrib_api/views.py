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

class masters_viewset(viewsets.ModelViewSet):
    queryset = Masters.objects.all()
    serializer_class = Masters_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = MastersFilter

class playbook_viewset(viewsets.ModelViewSet):
    queryset = Playbook.objects.all()
    serializer_class = Playbook_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = PlaybookFilter

class hosts_viewset(viewsets.ModelViewSet):
    queryset = Hosts.objects.all()
    serializer_class = Hosts_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = HostsFilter

def index(request):
    return render(request,'index.html')

def Write_to_redis(request):
    dics = {}
    if request.method == 'POST':
        dics = eval(json.dumps(request.POST))
        try:
            for k,val in dics.items():
                print k,val
                if k != 'csrfmiddlewaretoken':
                    cache.set(k,val)
        except Exception,e:
            return render(request,'basex.html',{'sdf':dics})


def Get_from_redis(request,*args):
    dicc = {}
    for i in args:
        try:
            dicc[i] = cache.get(i)
        except Exception,e:
            return render(request,'basex.html',{'sdf':e})
    return render(request,'basex.html',{'sdf':dicc})

def basex(request):
    dicx = {}
    if request.method == 'POST':
        dicx = eval(json.dumps(request.POST))
        try:
            for k,val in dicx.items():
                print k,val
                if k != 'csrfmiddlewaretoken':
                    cache.set(k,val)
        except Exception,e:
            return  render(request,'basex.html',{'sdf':e})
    return render(request,'basex.html',{'sdf':dicx})