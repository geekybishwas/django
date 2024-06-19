from django.db import models
from datetime import datetime
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    body=models.CharField(max_length=1000)
    # desc=models.CharField(max_length=1000)
    # It allwos the field to be left blank
    created_at=models.DateTimeField(default=datetime.now,blank=True)

class Room(models.Model):
    name=models.CharField(max_length=100)
class Message(models.Model):
    value=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
