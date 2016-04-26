from django.db import models
from abstract.models import CommonModel,NameModel
import uuid

class Play_type(NameModel):
    pass

class Status(NameModel):
    pass

class PlayBook(NameModel):
    type = models.ForeignKey(Play_type)

class Ipv4Address(NameModel):
    class Meta:
        ordering = ['name', ]

class Ipv4Network(NameModel):
    gateway = models.CharField(max_length=18, null=True)
    class Meta:
        ordering = ['name', ]

class Group(NameModel):
    ips = models.ManyToManyField(Ipv4Address)
    remark = models.CharField(max_length=30)

class Mission(CommonModel):
    mark = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hosts = models.ManyToManyField(Ipv4Address)
    groups = models.ManyToManyField(Group)
    playbooks = models.ManyToManyField(PlayBook)
    version = models.CharField(max_length=50,null=False)
    status = models.ForeignKey(Status)
    remark = models.TextField(blank=True)
    def __unicode__(self):
        return str(self.mark)
    class Meta:
        ordering = ['-created_date', ]

class Sub_Mission(CommonModel):
    mission=models.ForeignKey(Mission)
    host = models.ForeignKey(Ipv4Address)
    status = models.ForeignKey(Status)
    remark = models.CharField(max_length=80,blank=True)

