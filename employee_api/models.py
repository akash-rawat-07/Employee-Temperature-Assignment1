from django.db import models
from datetime import datetime


# Create your models here.
class Employee(models.Model):
    empname = models.CharField(primary_key=True, max_length=100)
    empage = models.IntegerField()
    empdesignation = models.CharField(max_length=100)
    empgender = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"

    # def __str__(self):
    #     return self.empname


class Device(models.Model):
    devicemodel = models.IntegerField(primary_key=True, unique=True, blank=False)
    devicemanufacturer = models.CharField(max_length=100)
    devicetype = models.CharField(max_length=20)

    class Meta:
        db_table = "device"

    # def __str__(self):
    #     return self.devicemanufacturer


class Temperature(models.Model):
    empname = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True) # using foreign key referencing to 'Employee' class
    devicemodel = models.ForeignKey(Device, on_delete=models.CASCADE, null=True) # using foreign key referencing to 'Device' class
    emptemperature = models.FloatField()
    date = models.DateField()
    # date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = "temperature"

    # def __str__(self):
    #     return self.emptemperature



