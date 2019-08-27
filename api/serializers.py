"""Models"""
from rest_framework import serializers

class CustomEmployeeSerializer(serializers.Serializer):
    """Custom Serializations"""
    email = serializers.EmailField()
    name = serializers.CharField(max_length=30)
    company = serializers.CharField(max_length=30)
    code = serializers.CharField(max_length=10)