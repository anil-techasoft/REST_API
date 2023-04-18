from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions
from .models import Employee
from .serializers import EmployeeSerializer


# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]
