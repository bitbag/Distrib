from django.db import models
from datetime import datetime

class Service_type(models.Model):
    name=models.CharField(max_length=30)
    alise=models.CharField(max_length=30)

class Status(models.Model):
    name=models.CharField(max_length=30)
    alise=models.CharField(max_length=30)

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