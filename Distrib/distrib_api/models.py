#coding:GBK
from django.db import models
from datetime import datetime

# class Service_type(models.Model):
#     name = models.CharField(max_length=30)
#     alias = models.CharField(max_length=30)
#     def __unicode__(self):
#         return self.alias
#
# class Status(models.Model):
#     name = models.CharField(max_length=30)
#     alias = models.CharField(max_length=30)
#     def __unicode__(self):
#         return self.alias

class Miss(models.Model):
    hosts = models.TextField()
    playbooks = models.TextField()
    version = models.CharField(max_length=50,null=False)
    status = models.CharField(max_length=20)
    uniquevalue = models.CharField(max_length=30,default=None)
    release_time = models.CharField(max_length=30,default=None)
    finish_time = models.CharField(max_length=30,default=None)
    remark = models.CharField(max_length=80,blank=True)

class SubMiss(models.Model):
    host = models.CharField(max_length=15)
    playbooks = models.TextField()
    version = models.CharField(max_length=50,null=False)
    status = models.CharField(max_length=20)
    uniquevalue = models.CharField(max_length=30,default=None)
    release_time = models.CharField(max_length=30,default=None)
    finish_time = models.CharField(max_length=30,default=None)
    remark = models.CharField(max_length=80,blank=True)

class log(models.Model):
    mission = models.TextField()
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=30)

class Masters(models.Model):
    master_id = models.AutoField(primary_key=True)
    master_name = models.CharField(max_length=50)
    master_ip = models.CharField(max_length=20)
    master_location = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    def __unicode__(self):
        return self.master_ip

class PlayBook(models.Model):
    play_name = models.CharField(max_length=40,default=None)
    play_type = models.CharField(max_length=30,default=None)
    def __unicode__(self):
        return self.play_name

class Hosts(models.Model):
    host_id = models.AutoField(primary_key=True)
    host_name = models.TextField()
    host_ip = models.CharField(max_length=20)
    host_group = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)

