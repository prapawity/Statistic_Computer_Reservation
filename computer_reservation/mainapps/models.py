from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Computer(models.Model):
    status = models.BooleanField(default=True)
class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    year = models.IntegerField()
class Reservation(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer,on_delete=models.CASCADE)
    date = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)

