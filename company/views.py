"""Company Views"""
from rest_framework import generics
from .serializers import CompanySerializer
from .models import Company

# Create your views here.

class CompanyListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



