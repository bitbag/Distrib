
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

class Masters_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Masters
        fields = ('url','master_name','master_ip','master_location','remark')

class PlayBook_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayBook
        fields = ('url','play_name','play_type')

class Hosts_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hosts
        fields = ('url','host_name','host_ip','host_group','remark')