"""Employee Views"""
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import EmployeeSerializer, UserSerializer
from .models import Employee
from django.contrib.auth.models import User
from django.core.exceptions import *

# Create your views here.

class EmployeeListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        queryset = Employee.objects.all()        
        username = self.request.query_params.get('username', None)
        if username is not None:
            userid = User.objects.get(username=username)
            queryset = queryset.filter(user=userid)
            #queryset = Employee.object.filter(user=userid)
        return queryset

class EmployeeViewByUserId(generics.RetrieveAPIView):
#class EmployeeViewByUserId(generics.ListAPIView):
    """Get Employee By email address"""
    lookup_field = "user"
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeViewByEmail(generics.ListAPIView):
    """Get Employee By email address"""
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        queryset = Employee.objects.all()        
        #username = self.lookup_url_kwarg("username")
        username = self.request.query_params.get('username', None)
        if username is not None:
            userid = User.objects.get(username=username)
            queryset = queryset.filter(user=userid)
            #queryset = Employee.object.filter(user=userid)
        else: 
            queryset = Employee.objects.none()
        
        return queryset
