from django.db import models
from datetime import datetime   
# Create your models here.
class user(models.Model):
    username= models.CharField(max_length=50)
    email=  models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    createdTime= models.DateTimeField(default=datetime.now, blank=True)
