from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer

# Create your views here.
class employeeList(APIView):
       def get(self, request):
           employee1 = employee.objects.all()
           serializer_class = employeeSerializer

           serializer = employeeSerializer(employee1, many= True)
           return Response(serializer.data)


       def post(self):
           pass
