
__author__ = 'Administrator'

from rest_framework import serializers
from distrib_api.models import Miss, Service_type, Status


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