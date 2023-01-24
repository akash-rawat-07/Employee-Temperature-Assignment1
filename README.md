# Project :
“Employee Temperature Records”


# Project Description :
In this project, I have created three models namely-Employee, Device, and Temperature and created a rest-api for all these three model to enter the attributes on all these three models. To store all the records of these three models, I have used “MySql” database to save the records.


# Features :
1.	User can perform Create, Read, Update, Delete operations on all three models.
2.	An Endpoint is created to get all the temperatures recorded for a particular employee
3.	with date filters.  
4.	An Endpoint is created which outputs the employees whose temperatures were more than 100°F for a particular date.


# Assignment Endpoints :
1. Create 3 different Insert Endpoints for all the models so that client can add the data
in the database and populate it with some random data.
ENDPOINT :
"Employee" Model Insertion Endpoint    =    "localhost:8000/createemployee/"
"Device" Model Insertion Endpoint      =    "localhost:8000/createemployee/"
"Temperature" Model Insertion Endpoint =    "localhost:8000/createemployee/"
2. Create an Endpoint to get all the temperatures recorded for a particular employee
with date filters.
ENDPOINT :  "localhost:8000/hightempempdate/emp_name/date/"
Example  :  "localhost:8000/hightempempdate/akash/2022-12-30/"
3. Create an Endpoint which outputs the employees whose temperatures were more
than 100°F for a particular date.
ENDPOINT :  "localhost:8000/hightempemp/date/"
Example  :  "localhost:8000/hightempemp/2022-12-29/"


# Prerequisites :
Be sure you have the following installed on your development machine:
1.	Python  3.10 version
2.	Virtualenv
3.	pip


# Requirements :
1.	Django==4.1.3
2.	djangorestframework==3.14.0
3.	mysqlclient==2.1.1


# Django Installation Steps :-
1.	Install Python 3.10
2.	Install Django version 4.1.3
3.	Install all dependencies cmd -python -m pip install –-user -r requirements.txt
4.	Finally run cmd - python manage.py runserver

