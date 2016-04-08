
__author__ = 'Administrator'

from rest_framework import serializers
from distrib_api.models import *


class Miss_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miss
        fields = ('url','group','type','version','status','remark')

class Service_type_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_type
        fields = ('url','name','alias')

class Status_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('url','name','alias')

class log_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = log
        fields = ('url','mission','start_time','end_time','status')

class Master_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = ('url','host_name','host_ip','host_location','remark')

class Playbook_ser(serializers.HyperlinkedModelSerializer):
    p_type=serializers.SlugRelatedField(queryset=Master.objects.all(), many=True,slug_field='host_ip')
    class Meta:
        model = Playbook
        fields = ('url','p_name','p_type')

class Hosts_ser(serializers.HyperlinkedModelSerializer):
    host_name = serializers.SlugRelatedField(queryset=Master.objects.all(), slug_field='host_ip')
    class Meta:
        model = Hosts
        fields = ('url','host_name','host_id','host_ip','host_group','remark')