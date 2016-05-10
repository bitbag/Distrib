# -*- coding: utf-8 -*-
from django.db.models.signals import post_save,m2m_changed
from django.dispatch import receiver
from distrib_api.models import Mission,Sub_Mission,Status,Ipv4Address
from .tasks import create_sub_mission

def progress_rebuild(mission):
    try:
        all_host = []
        for single_host in mission.hosts.all():
            all_host.append(single_host)
        for group in mission.groups.all():
            for group_host in group.ips.all():
                all_host.append(group_host)
        all_host_list = list(set(all_host))
        existed_host_list=list(set([x.host for x in Sub_Mission.objects.filter(mission=mission)]))
        add_list = [x for x in all_host_list if x not in existed_host_list]
        del_list = [x for x in existed_host_list if x not in all_host_list]
        if add_list:
            for add_host in add_list:
                Sub_Mission.objects.create(host=add_host, mission=mission, status=Status.objects.get(name='undo'))
        if del_list:
            for del_host in del_list:
                Sub_Mission.objects.filter(host=del_host, mission=mission).delete()
        mission.status=Status.objects.get(name='undo')
        mission.save()
    except Exception,e:
        mission.status=Status.objects.get(name='init_failed')
        mission.save()


def mission_change(sender, **kwargs):
    mission=kwargs['instance']
    if kwargs['action']=='post_add':
        return progress_rebuild(mission)


# @receiver(post_save, sender=Mission)
# def add_aub_mission(**kwargs):
#     if kwargs['created']:
#         instance=kwargs['instance']
#         mark=instance.mark
#         return create_sub_mission.apply_async(args=(mark,), countdown=10)
#
m2m_changed.connect(mission_change,sender=Mission.hosts.through)
m2m_changed.connect(mission_change,sender=Mission.groups.through)




