from django.db import models

# Create your models here.

class Student(models.Model):
    studRegno = models.IntegerField()
    studName = models.CharFeild(max_length=20)
    studCgpa = models.FloatField()
