"""Employee Views"""
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import CustomEmployeeSerializer
from employee.models import Employee
from company.models import Company
from django.contrib.auth.models import User
from django.core.exceptions import *

# Create your views here.

class CustomEmployeeData(object):
    def __init__(self, email, name, company, code):
        self.email = email
        self.name = name
        self.company = company
        self.code = code

class CustomEmployeeView(views.APIView):
    """Custom View"""
    def get(self, request, *args, **kwargs):
        username = self.request.query_params.get('username', None)
        if username is not None:
            try:
                user = User.objects.get(username=username)
                employee = Employee.objects.get(user=user)
                try:
                    company = Company.objects.get(employee=employee)
                    companyname = company.name
                except ObjectDoesNotExist:
                    companyname = ""
                
                name = "%s %s" % (user.first_name, user.last_name)
                customdata = CustomEmployeeData(user.email, name, companyname, employee.code)
                result = CustomEmployeeSerializer(customdata).data

            except ObjectDoesNotExist:
                customdata = CustomEmployeeData("","","","")
                result = CustomEmployeeSerializer(customdata).data
        else:
            customdata = CustomEmployeeData("","","","")
            result = CustomEmployeeSerializer(customdata).data

        return Response(result)
