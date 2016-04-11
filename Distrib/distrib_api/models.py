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
    type=models.TextField()
    version=models.CharField(max_length=80)
    status=models.CharField(max_length=20)
    remark=models.CharField(max_length=80)

class log(models.Model):
    mission=models.TextField()
    start_time=models.DateTimeField(default=datetime.now())
    end_time=models.DateTimeField(default=datetime.now())
    status=models.CharField(max_length=30)

class Master(models.Model):
    master_host_name = models.CharField(max_length=50)
    master_host_ip = models.CharField(max_length=20)
    master_host_location = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)
    def __unicode__(self):
        return self.master_host_ip

class PlayBook(models.Model):
    play_name = models.CharField(max_length=40,default=None)
    play_type = models.CharField(max_length=30,default=None)
    def __unicode__(self):
        return self.play_name

class Host(models.Model):
    host_name = models.TextField()
    host_ip = models.CharField(max_length=20)
    host_group = models.CharField(max_length=30)
    remark = models.CharField(max_length=30)

