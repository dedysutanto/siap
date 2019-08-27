"""Employee urls routing"""
from django.urls import path
from .views import EmployeeListView

urlpatterns = [
    path('employee/', EmployeeListView.as_view(), name="employee-all"),
    #path('employee/<int:user>/', EmployeeViewByUserId.as_view(), name="employee-by-userid"),
    #path('getemployee/', EmployeeViewByEmail.as_view(), name="employee-by-email"),
]
