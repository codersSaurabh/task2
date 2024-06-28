from django.db import models

# Create your models here.
class doctor(models.Model):
    FName=models.CharField(max_length=200,null=False,blank=False)
    LName=models.CharField(max_length=200,null=False,blank=False)
    Password=models.CharField(max_length=20,null=False,blank=False)
    Email=models.EmailField(null=False,blank=False)
    Address=models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=100,null=False,blank=False,default="")
    state=models.CharField(max_length=100,null=False,blank=False,default="")
    pincode=models.CharField(max_length=8,null=False,blank=False,default="")
    Profile=models.ImageField(upload_to="images")
    Username=models.CharField(max_length=100,null=False,blank=False)
   

    def __str__(self) -> str:
        return self.Username

class Patient(models.Model):
    FName=models.CharField(max_length=200,null=False,blank=False)
    LName=models.CharField(max_length=200,null=False,blank=False)
    Password=models.CharField(max_length=20,null=False,blank=False)
    Email=models.EmailField(null=False,blank=False)
    Address=models.CharField(max_length=100,null=False,blank=False)
    city=models.CharField(max_length=100,null=False,blank=False,default="")
    state=models.CharField(max_length=100,null=False,blank=False,default="")
    pincode=models.CharField(max_length=8,null=False,blank=False,default="")
    Profile=models.ImageField(upload_to="images")
    Username=models.CharField(max_length=100,null=False,blank=False)

   

    def __str__(self) -> str:
        return self.Username