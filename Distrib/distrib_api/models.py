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

class Masters(models.Model):
    master_id = models.AutoField(primary_key=True)
    master_host_name = models.CharField(max_length=50)
    master_host_ip = models.CharField(max_length=20)
    master_host_location = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    def __unicode__(self):
        return self.master_host_ip

class Playbook(models.Model):
    p_name = models.CharField(max_length=20)
    p_type = models.ManyToManyField(Masters)
    def __unicode__(self):
        return self.p_name

class Hosts(models.Model):
    host_name = models.ForeignKey(Masters)
    host_id = models.AutoField(primary_key=True)
    host_ip = models.CharField(max_length=20)
    host_group = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)

