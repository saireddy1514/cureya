from django.db import models
from django.contrib.auth.models import User
from django_random_id_model import RandomIDModel
class Registration(RandomIDModel):
    name=models.CharField(max_length=200)
    genders = [
    (None, 'Choose your gender'),
    ('male', 'male'),
    ('female', 'female'),
    ('custom', 'custom'),
    ('Prefer Not To Say', 'Prefer Not To Say'),
    ]
    gender=models.CharField(max_length=200,choices=genders)
    email=models.EmailField(max_length=200)
    phoneno=models.CharField(max_length=12)
    password=models.CharField(max_length=100)
    patid=models.CharField(max_length=100,default='')
    is_active=models.BooleanField(default=False)
    mob_is_active=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class DoctorRegistration(RandomIDModel):
    docid=models.CharField(max_length=100,default='')
    name=models.CharField(max_length=200)
    genders = [
    (None, 'Choose your gender'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]
    gender=models.CharField(max_length=200,choices=genders)
    email=models.EmailField(max_length=200)
    phoneno=models.CharField(max_length=12)
    experience=models.CharField(max_length=10)
    workfield=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    password=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    mob_is_active=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"

class OTPVerification(models.Model):
    phoneno=models.CharField(max_length=100)
    otp=models.CharField(max_length=100)
    pid=models.CharField(max_length=100,default='00000')