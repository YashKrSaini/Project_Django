from django.db import models

# Create your models here.
class userData(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=30)
    email=models.EmailField()
    dob=models.CharField(max_length=30)
    passWord=models.CharField(max_length=20)
    image=models.ImageField(upload_to="" ,default="")
    
    def __str__(self):
        return (self.name+' : '+self.email)