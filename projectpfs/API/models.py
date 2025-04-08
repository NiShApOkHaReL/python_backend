from django.db import models
from django.utils import timezone


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=100)
    prog = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True,default=timezone.now)


