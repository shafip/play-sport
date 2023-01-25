from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Productmodel(models.Model):
    id=models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='images')
    name=models.CharField(max_length=150)
    place=models.CharField(max_length=200)
    price=models.CharField(max_length=4)

    def __str__(self):
        return self.name

class RegisterForm(models.Model):
    id = models.AutoField(primary_key=True)

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    place = models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)



