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