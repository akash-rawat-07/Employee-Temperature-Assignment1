from django.contrib import admin
from .models import Employee, Device, Temperature

# Register your models here.
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(Temperature)
