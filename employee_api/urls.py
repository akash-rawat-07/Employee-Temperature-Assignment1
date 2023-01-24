from django.urls import path
from .views import index, employee_list, employee_detail, createEmployee, deleteEmployee, updateEmployee, createDevice, allDevices, singleDevice, updateDevice,deleteDevice, createTemp, allTemp, getsingletemp, updateTemp, deleteTemp, highTempEmp, allhightempemp, hightempempdate
# from . import views
urlpatterns = [
    path('', index),
    path('employee_list/', employee_list),
    path('employee_detail/<str:empname>/', employee_detail),
    path('createemployee/', createEmployee),
    path('deleteemployee/<str:empname>/', deleteEmployee),
    path('updateemployee/<str:empname>/', updateEmployee),
    
    path('createdevice/', createDevice),
    path('device_list/', allDevices),
    path('device/<int:devicemodel>/', singleDevice),
    path('updatedevice/<int:devicemodel>/', updateDevice),
    path('deletedevice/<int:devicemodel>/', deleteDevice),

    path('createtemp/', createTemp),
    path('getalltemp/', allTemp),
    path('singletemp/<str:empname>/', getsingletemp),
    path('updatetemp/<int:pk>/', updateTemp),
    path('deletetemp/<int:pk>/', deleteTemp),

    path('hightempemp/<str:mydate>/', highTempEmp),
    path('allhightempemp/<str:mydate>/', allhightempemp),
    path('hightempempdate/<str:empname>/<str:mydate>/', hightempempdate)
]
