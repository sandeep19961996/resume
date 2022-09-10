from email import message
from django.db import models

# Create your models here.
class Contact_me(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)