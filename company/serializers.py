"""Models"""
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    """Company Serializations"""

    class Meta:
        model = Company
        fields = "__all__"