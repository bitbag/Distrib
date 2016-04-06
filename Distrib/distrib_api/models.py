from django.db import models
from datetime import datetime

class Service_type(models.Model):
    name=models.CharField(max_length=30)
    alias=models.CharField(max_length=30)
    def __unicode__(self):
        return self.alias

class Status(models.Model):
    name=models.CharField(max_length=30)
    alias=models.CharField(max_length=30)
    def __unicode__(self):
        return self.alias

class Miss(models.Model):
    group=models.TextField()
    type=models.ForeignKey(Service_type)
    version=models.CharField(max_length=80)
    status=models.ForeignKey(Status)
    remark=models.CharField(max_length=80)

class log(models.Model):
    mission=models.ForeignKey(Miss)
    start_time=models.DateTimeField(default=datetime.now())
    end_time=models.DateTimeField(default=datetime.now())
    status=models.CharField(max_length=30)

class Master(models.Model):
    host_name = models.CharField(max_length=50)
    host_ip = models.CharField(max_length=20)
    host_location = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    def __unicode__(self):
        return self.host_ip

class Playbook(models.Model):
    p_name = models.CharField(max_length=20)
    p_type = models.ManyToManyField(Master)
    def __unicode__(self):
        return self.p_name

# class Host(models.Model):
#     note_host_name = models.ForeignKey(Master)
#     note_host_ip = models.CharField(max_length=20)
#     host_group = models.CharField(max_length=30)
#     remark = models.CharField(max_length=30)
class Hosts(models.Model):
    note_host_name = models.ForeignKey(Master)
    note_host_id = models.IntegerField(primary_key=True)
    note_host_ip = models.CharField(max_length=20)
    host_group = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)

