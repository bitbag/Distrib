#coding=utf8
# Create your views here.
from rest_framework import viewsets
from rest_framework import filters as source_filter
import rest_framework_filters as filters
from rest_framework_filters.backends import DjangoFilterBackend
from serializers import *
from models import *
from filters import *
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes


class SearchViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,source_filter.SearchFilter)

    def perform_create(self, serializer):
        return super(SearchViewSet, self).perform_create(serializer)

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissions,)
    filter_backends = (DjangoFilterBackend,)

    def perform_create(self, serializer):
        return super(BaseViewSet, self).perform_create(serializer)


class StatusViewSet(BaseViewSet):
    http_method_names = ['post', 'get', 'put', 'patch']
    queryset = Status.objects.all()
    serializer_class = Statusserializers
    filter_fields = ('name',)

class Play_typeViewSet(BaseViewSet):
    http_method_names = ['post', 'get', 'put', 'patch']
    queryset = Play_type.objects.all()
    serializer_class = Play_typeserializers
    filter_fields =('name',)

class GroupViewSet(BaseViewSet):
    http_method_names = ['post', 'get', 'put', 'patch']
    queryset = Group.objects.all()
    serializer_class = Groupserializers
    filter_fields = ('name',)

class PlaybookViewSet(BaseViewSet):
    http_method_names = ['post', 'get', 'put', 'patch']
    queryset = PlayBook.objects.all()
    serializer_class = PlayBookserializers
    fiter_class=Play_bookFilter

class MissionViewSet(BaseViewSet):
    http_method_names = ['get','post', 'put', 'patch']
    queryset = Mission.objects.all()
    serializer_class = Missionserializers
    filter_class=MissionFilter

class Sub_missionViewSet(BaseViewSet):
    http_method_names = ['get', 'put', 'patch']
    queryset = Sub_Mission.objects.all()
    serializer_class = Sub_Missionserializers
    filter_class=Sub_missionFilter

class Ipv4AddressViewSet(SearchViewSet):
    http_method_names = ['post', 'get']
    queryset=Ipv4Address.objects.all()
    serializer_class = IPv4AddressSerializer
    filter_fields = ('name',)
    search_fields = ('^name', )


class Ipv4NetworkViewSet(BaseViewSet):
    http_method_names = ['post', 'get']
    queryset=Ipv4Network.objects.all()
    serializer_class = IPv4NetworkSerializer

# def CreateMission(request):
#     if request.method == 'GET':
#         return render(request,'index.html')
#     elif request.method == 'POST':
#         try:
#             HostList = list(set([ host for host in request.REQUEST.get('hostlist').split(',')]))
#             PlaybookList = list(set([playbook for playbook in request.REQUEST.get('playbook').split(',')]))
#             Version = request.REQUEST.get('version')
#             UniqueValue = datetime.now().strftime("%Y%m%d%H%M%S")
#             status = {
#                 '0':'unexecuted',
#                 '1':'executing',
#                 '2':'executed',
#                 '3':'failed',
#                 '4':'unknown',
#             }
#             remark = request.REQUEST.get('remark')
#             try:
#                 print r'=====================开始生成主任务==================='
#                 Miss.objects.create(hosts=HostList,playbooks=PlaybookList,version=Version,status=status['0'],uniquevalue=UniqueValue,release_time=datetime.now(),finish_time='unknown',remark=remark)
#                 print '======================主任务已生成====================='
#                 if PlaybookList:
#                     try:
#                         for host in HostList:
#                             SubMiss.objects.create(host=host,playbooks=PlaybookList,release_time=datetime.now(),finish_time='unknown',status=status['0'],uniquevalue=UniqueValue)
#                         print '======================子任务已生成====================='
#                     except Exception,error:
#                         print "==============子任务生成失败 %s===================" % error
#                 else:
#                     print "==================PlaybookList is Null============"
#             except Exception,error:
#                 print '====================Create mission failed! %s======================' % error
#         except Exception,error:
#             print '===============No host or playbook selected! %s==========================' % error
#         return render(request,'basex.html',{'sdf':(PlaybookList,HostList,Version)})
#     else:
#         return render(request,'basex.html',{'sdf':'error'})
#
# def Write_to_redis(request):
#     dics = {}
#     if request.method == 'POST':
#         dics = eval(json.dumps(request.POST))
#         try:
#             for k,val in dics.items():
#                 print k,val
#                 if k != 'csrfmiddlewaretoken':
#                     cache.set(k,val)
#         except Exception,e:
#             return render(request,'basex.html',{'sdf':dics})
#
#
# def Get_from_redis(request,*args):
#     dicc = {}
#     for i in args:
#         try:
#             dicc[i] = cache.get(i)
#         except Exception,e:
#             return render(request,'basex.html',{'sdf':e})
#     return render(request,'basex.html',{'sdf':dicc})
#
# def basex(request):
#     dicx = {}
#     if request.method == 'POST':
#         dicx = eval(json.dumps(request.POST))
#         try:
#             for k,val in dicx.items():
#                 print k,val
#                 if k != 'csrfmiddlewaretoken':
#                     cache.set(k,val)
#         except Exception,e:
#             return  render(request,'basex.html',{'sdf':e})
#     return render(request,'basex.html',{'sdf':dicx})