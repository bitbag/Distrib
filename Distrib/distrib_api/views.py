#coding:GBK
from django.shortcuts import render_to_response,render
from distrib_api.serializers import *
from distrib_api.models import *
from rest_framework import viewsets
from rest_framework_filters import backends
import rest_framework_filters as filters
from .filters import *
from datetime import datetime

# class seria_viewset(viewsets.ModelViewSet):
#     queryset = Service_type.objects.all()
#     serializer_class = Service_type_ser
#     filter_backends = (backends.DjangoFilterBackend, )
#     filter_class = ServiceTypeFilter

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

class submiss_viewset(viewsets.ModelViewSet):
    queryset = SubMiss.objects.all()
    serializer_class = SubMiss_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = SubMissFilter

# class status_viewset(viewsets.ModelViewSet):
#     queryset = Status.objects.all()
#     serializer_class = Status_ser
#     filter_backends = (backends.DjangoFilterBackend, )
#     filter_class = StatusFilter

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
    queryset = PlayBook.objects.all()
    serializer_class = PlayBook_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = PlaybookFilter

class hosts_viewset(viewsets.ModelViewSet):
    queryset = Hosts.objects.all()
    serializer_class = Hosts_ser
    filter_backends = (backends.DjangoFilterBackend, )
    filter_class = HostsFilter

def index(request):
    return render(request,'index.html')


def CreateMission(request):
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        try:
            HostList = list(set([ host for host in request.REQUEST.get('hostlist').split(',')]))
            PlaybookList = list(set([playbook for playbook in request.REQUEST.get('playbook').split(',')]))
            Version = request.REQUEST.get('version')
            UniqueValue = datetime.now().strftime("%Y%m%d%H%M%S")
            status = {
                '0':'unexecuted',
                '1':'executing',
                '2':'executed',
                '3':'failed',
                '4':'unknown',
            }
            remark = request.REQUEST.get('remark')
            try:
                print r'=====================开始生成主任务==================='
                Miss.objects.create(hosts=HostList,playbooks=PlaybookList,version=Version,status=status['0'],uniquevalue=UniqueValue,release_time=datetime.now(),finish_time='unknown',remark=remark)
                print '======================主任务已生成====================='
                if PlaybookList:
                    try:
                        for host in HostList:
                            SubMiss.objects.create(host=host,playbooks=PlaybookList,release_time=datetime.now(),finish_time='unknown',status=status['0'],uniquevalue=UniqueValue)
                        print '======================子任务已生成====================='
                    except Exception,error:
                        print "==============子任务生成失败 %s===================" % error
                else:
                    print "==================PlaybookList is Null============"
            except Exception,error:
                print '====================Create mission failed! %s======================' % error
        except Exception,error:
            print '===============No host or playbook selected! %s==========================' % error
        return render(request,'basex.html',{'sdf':(PlaybookList,HostList,Version)})
    else:
        return render(request,'basex.html',{'sdf':'error'})

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