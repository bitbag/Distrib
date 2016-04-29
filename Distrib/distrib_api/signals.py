# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from distrib_api.models import Mission,Sub_Mission,Status

def create_sub_mission(new_mission):
    all_host=[]
    print new_mission.mark
    mission=Mission.objects.get(mark=new_mission.mark)
    print mission
    print mission.hosts.iterator()
    for single_host in mission.hosts.all():
        all_host.append(single_host)

    for group in mission.groups.all():
        for group_host in group.ips.all():
            all_host.append(group_host)
    print all_host
    all_host_list = list(set(all_host))
    print all_host_list
    for host in all_host_list:
        Sub_Mission.objects.create(host=host,mission=mission,status=Status.objects.get(name='undo'))


@receiver(post_save, sender=Mission)
def add_aub_mission(**kwargs):
    print kwargs
    print kwargs['instance'].hosts.all()
    # if created:
    #     return create_sub_mission(instance)

