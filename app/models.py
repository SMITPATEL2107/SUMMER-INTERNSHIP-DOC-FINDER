from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique= True)
    password = models.CharField(max_length = 20)
    role = models.CharField(max_length = 10)

class Doctor(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    qualification = models.CharField(max_length=100, blank= True)
    speciality = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 10)
    clinic = models.CharField(max_length= 100,blank = True)
    address = models.CharField(max_length= 500, blank= True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank= True)
    gender = models.CharField(max_length= 10)
    birthdate = models.DateField()
    location = models.CharField(max_length= 30, blank= True)
    about_doc = models.CharField(max_length= 100, blank= True)

class Patient(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length= 500, blank = True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50, blank = True)
    gender = models.CharField(max_length= 10)
    birthdate = models.DateField()