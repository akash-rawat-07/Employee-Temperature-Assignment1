from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Employee, Device, Temperature
from .serializers import EmployeeSerializer, DeviceSerializer, TemperatureSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request, 'index.html')


# Get all Employee details
@api_view(['GET'])
def employee_list(request):
    # if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


# Get single employee detail
@api_view(['GET'])
def employee_detail(request, empname):
    try:
        employee = Employee.objects.get(empname=empname)

    except Employee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


# Creating single employee
@api_view(['POST'])
def createEmployee(request):
    if request.method=='POST':
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete single employee
@api_view(['Delete'])
def deleteEmployee(request, empname):
    try:
        employee = Employee.objects.get(empname=empname)
    except Employee.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method=='DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Update employee
@api_view(['PUT'])
def updateEmployee(request, empname):
    try:
        employee = Employee.objects.get(empname=empname)
    except:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

#  Device Section

# Create device
@api_view(['POST'])
def createDevice(request):
    if request.method == 'POST':
        serializer = DeviceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get all device
@api_view(['GET'])
def allDevices(request):
    if request.method == 'GET':
        device = Device.objects.all()
        serializer = DeviceSerializer(device, many=True)
        return Response(serializer.data)

# Get single device
@api_view(['GET'])
def singleDevice(request, devicemodel):
    try:
        device = Device.objects.get(devicemodel=devicemodel)
    except Device.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

# Update device
@api_view(['PUT'])
def updateDevice(request, devicemodel):
    try:
        device = Device.objects.get(devicemodel=devicemodel)
    except Device.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = DeviceSerializer(device, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete device
@api_view(['DELETE'])
def deleteDevice(request, devicemodel):
    try:
        device = Device.objects.get(devicemodel=devicemodel)
    except Device.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Temperature Section

# Create Temperature
@api_view(['POST'])
def createTemp(request):
     if request.method == 'POST':
         serializer = TemperatureSerializer(data=request.data)

         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get all Temperature
@api_view(['GET'])
def allTemp(request):
    if request.method == 'GET':
        temp = Temperature.objects.all()
        serializer = TemperatureSerializer(temp, many=True)
        return Response(serializer.data)


# Get single Temperature
@api_view(['GET'])
def getsingletemp(request, empname):
    if request.method == 'GET':  
        temp = Temperature.objects.filter(empname=empname)
        serializer = TemperatureSerializer(temp, many=True)
        return Response(serializer.data)


# Update device
@api_view(['PUT'])
def updateTemp(request, pk):
    try:
        temp = Temperature.objects.get(id=pk)
    except Device.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = TemperatureSerializer(temp, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete device
@api_view(['DELETE'])
def deleteTemp(request, pk):
    try:
        temp = Temperature.objects.get(id=pk)
    except Device.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        temp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Assignment points:

# Employees having Temperature more than 100F with specific date
@api_view(['GET'])
def highTempEmp(request, mydate):
    temp = Temperature.objects.filter(date=mydate, emptemperature__gt=100)
    serializer = TemperatureSerializer(temp, many=True)
    return Response(serializer.data)


# All Employees having Temperature more than 100F 
@api_view(['GET'])
def allhightempemp(request):
    temp = Temperature.objects.filter(emptemperature__gt=100)
    serializer = TemperatureSerializer(temp, many=True)
    return Response(serializer.data)

# temperatures recorded for a particular employee with date filters
@api_view(['GET'])
def hightempempdate(request, empname, mydate):
    temp = Temperature.objects.filter(empname=empname, date=mydate)
    serializer = TemperatureSerializer(temp, many=True)
    return Response(serializer.data)