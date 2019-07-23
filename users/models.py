from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=100)
    sex = models.CharField(choices= [('man','男'),('woman','女')],max_length=10)
    datadate = models.DateField(auto_now_add=True,auto_created=True)