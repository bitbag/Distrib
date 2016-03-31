
__author__ = 'Administrator'

from rest_framework import serializers
from distrib_api.models import *


class Miss_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Miss
        fields = ('group','type','version','status','remark')

class Service_type_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service_type
        fields = ('name','alise')

class Status_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('name','alise')

class log_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = log
        fields = ('mission','start_time','end_time','status')

class Master_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Master
        fields = ('host_name','host_ip','host_location','remark')

class Playbook_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playbook
        fields = ('p_name','p_type')

class Host_ser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('note_host_name','note_host_ip','host_group','remark')