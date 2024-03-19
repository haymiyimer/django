
from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=20,blank=False)
    phone=models.IntegerField()
    email=models.EmailField(blank=False)
    image=models.ImageField(upload_to='images/',blank="default.jpg")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=20,blank=False)
    tsc_no = models.IntegerField()
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.name

