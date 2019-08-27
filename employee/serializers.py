"""Models"""
from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """User Serializations"""

    class Meta:
        model = User
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    """Employee Serializations"""

    class Meta:
        model = Employee
        fields = "__all__"
        