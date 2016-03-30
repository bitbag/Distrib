from django.shortcuts import render_to_response
from distrib_api.serializers import Miss_ser, Service_type_ser, Status_ser
from distrib_api.models import Miss, Service_type, Status
from rest_framework import viewsets

class seria_viewset(viewsets.ModelViewSet):
    queryset = Service_type.objects.all()
    serializer_class = Service_type_ser

class miss_viewset(viewsets.ModelViewSet):
    queryset = Miss.objects.all()
    serializer_class = Miss_ser

class status_viewset(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = Status_ser

def index(request):
    strs = Miss.objects.all()
    return render_to_response('index.html',{'strs':strs})