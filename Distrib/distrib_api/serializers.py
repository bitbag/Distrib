
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
        fields = ('url','master_host_name','master_host_ip','master_host_location','remark')

class PlayBook_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayBook
        fields = ('url','play_name','play_type')

class Host_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('url','host_name','host_ip','host_group','remark')