from rest_framework import filters as source_filter
import rest_framework_filters as filters
from rest_framework_filters.backends import DjangoFilterBackend


from models import *

# class BaseViewSet(viewsets.ModelViewSet):
class Play_typeFilter(filters.FilterSet):
    name = filters.CharFilter(name="name")
    class Meta:
        model = Play_type
        fields = ['name']

class Play_bookFilter(filters.FilterSet):
    type = filters.CharFilter(name="type")
    class Meta:
        model = PlayBook
        fields = ['name','type']

class HostFilter(filters.FilterSet):
    name=filters.CharFilter(name="name")
    class Meta:
        model = Ipv4Address
        fields=['name']

class StatusFilter(filters.FilterSet):
    name = filters.CharFilter(name="name")
    class Meta:
        model = Status
        fields = ['name']

class MissionFilter(filters.FilterSet):
    status = filters.RelatedFilter(StatusFilter, name='status')
    mark=filters.CharFilter(name="mark")
    class Meta:
        model = Mission
        fields=['status','version','mark']

class Sub_missionFilter(filters.FilterSet):
    status = filters.RelatedFilter(StatusFilter, name='status')
    host = filters.RelatedFilter(HostFilter, name='host')
    mission = filters.RelatedFilter(MissionFilter,name='mission')
    class Meta:
        model = Sub_Mission
        fields = ['status', 'mission','host']
