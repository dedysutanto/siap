"""Employee urls routing"""
from django.urls import path
from .views import CustomEmployeeView

urlpatterns = [
    path('getemployee/', CustomEmployeeView.as_view(), name="getemployee-api")
]
