import django_filters
from rest_framework_filters import filters
from rest_framework_filters.filters import RelatedFilter, AllLookupsFilter
from rest_framework_filters.filterset import FilterSet, LOOKUP_SEP
from distrib_api.models import *

class ServiceTypeFilter(django_filters.FilterSet):
    name  = filters.CharFilter(name='name')

    class Meta:
        model = Service_type

class StatusFilter(django_filters.FilterSet):
    name = filters.CharFilter(name='name')

    class Meta:
        model = Status

class MissFilter(django_filters.FilterSet):
    group = filters.CharFilter(name='group')
    version = filters.CharFilter(name='version')

    class Meta:
        model = Miss

class LogFilter(django_filters.FilterSet):
    mission = filters.CharFilter(name='mission')
    status = filters.CharFilter(name='status')

    class Meta:
        model = log

class MastersFilter(django_filters.FilterSet):
    hostip = filters.CharFilter(name='host_ip')

    class Meta:
        model = Masters

class PlaybookFilter(django_filters.FilterSet):
    pname = filters.CharFilter(name='p_name')

    class Meta:
        model = Playbook


class HostsFilter(django_filters.FilterSet):
    hostip = filters.CharFilter(name='host_ip')

    class Meta:
        model = Hosts

