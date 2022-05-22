from django.shortcuts import render
from .serializer import InstallationSerializer,StatusSerializer
from rest_framework import viewsets
from.models import Installation,Status

# Create your views here.
class Viewinstallations(viewsets.ModelViewSet):
    
    queryset = Installation.objects.all()
    serializer_class = InstallationSerializer

class Viewstatus(viewsets.ModelViewSet):
    
    queryset = Status.objects.all().order_by('-id')
    serializer_class =  StatusSerializer
