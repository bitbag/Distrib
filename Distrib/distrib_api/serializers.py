from rest_framework import serializers
from netaddr import *
from distrib_api.models import *

class Play_typeserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Play_type

class Statusserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status


#class SubMiss_ser(serializers.HyperlinkedModelSerializer):
class PlayBookserializers(serializers.HyperlinkedModelSerializer):
    type = serializers.SlugRelatedField(queryset=Play_type.objects.all(), slug_field='name')
    class Meta:
        model = PlayBook

class Groupserializers(serializers.HyperlinkedModelSerializer):
    ips = serializers.SlugRelatedField(many=True, queryset=Ipv4Address.objects.all(), slug_field='name')
    class Meta:
        model = Group

class Missionserializers(serializers.HyperlinkedModelSerializer):
    hosts=serializers.SlugRelatedField(many=True, queryset=Ipv4Address.objects.all(), slug_field='name')
    playbooks=serializers.SlugRelatedField(many=True, queryset=PlayBook.objects.all(), slug_field='name')
    groups=serializers.SlugRelatedField(many=True, queryset=Group.objects.all(), slug_field='name')
    status=serializers.SlugRelatedField(queryset=Status.objects.all(), slug_field='name')
    sub_mission=serializers.SerializerMethodField()
    class Meta:
        model = Mission
        fields = ('url','mark','hosts','playbooks','groups','sub_mission','version','status','remark','created_date','modified_date')

    def get_sub_mission(self,obj):
        result=[]
        for m in Sub_Mission.objects.filter(mission=obj):
            data={}
            data['id']=m.id
            data['host']=m.host.name
            data['status']=m.status.name
            result.append(data)
        return result


class Sub_Missionserializers(serializers.ModelSerializer):
    host = serializers.SlugRelatedField(queryset=Ipv4Address.objects.all(), slug_field='name')
    status = serializers.SlugRelatedField(queryset=Status.objects.all(), slug_field='name')
    class Meta:
        model = Sub_Mission
        fields = ('url','mission','host','status','remark')

class IPv4AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ipv4Address

class IPv4NetworkSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ipv4Network

    def create(self, validated_data):
        print validated_data
        prefix = validated_data['name']
        nwk = IPNetwork(prefix)
        rawAddrs = [Ipv4Address(name=str(x)) for x in list(nwk)]
        addresses = Ipv4Address.objects.bulk_create(rawAddrs, batch_size=30)
        return super(IPv4NetworkSerializer, self).create(validated_data)