from django.shortcuts import render
from rest_framework import viewsets
from .models import FrontEnd
from .serializers import FrontEndSerializer 
# Create your views here.

class FrontEndView(viewsets.ModelViewSet):
    serializer_class=FrontEndSerializer
    queryset=FrontEnd.objects.all()
