from distrib_api.models import Mission,Sub_Mission,Status
from celery import shared_task

@shared_task
def create_sub_mission(mark):
    try:
        all_host=[]
        mission=Mission.objects.get(mark=mark)
        for single_host in mission.hosts.all():
            all_host.append(single_host)

        for group in mission.groups.all():
            for group_host in group.ips.all():
                all_host.append(group_host)
        all_host_list = list(set(all_host))
        for host in all_host_list:
            Sub_Mission.objects.create(host=host,mission=mission,status=Status.objects.get(name='undo'))
        Mission.objects.filter(mark=mark).update(status=Status.objects.get(name='undo'))
    except Exception,e:
        Mission.objects.filter(mark=mark).update(status=Status.objects.get(name='init_failed'))


