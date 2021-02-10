from django.db import models

# Create your models here.


class EmployeeModel(models.Model):
    code = models.BigIntegerField()
    person_type = models.CharField(max_length=10)
    fname = models.CharField(max_length=50)
    father = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    religion = models.CharField(max_length=10)
    sex = models.CharField(max_length=1)
    nation = models.CharField(max_length=50)
    age = models.IntegerField()
