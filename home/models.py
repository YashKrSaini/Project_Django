from django.db import models

# Create your models here.
class userData(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    dob=models.DateField()
    passWord=models.TextField(max_length=20)
    