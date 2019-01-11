from django.db import models

# Create your models here.


class Clinic(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinCode = models.IntegerField()

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pinCode = models.IntegerField()

    def __str__(self):
        return self.name
    
class BloodBank(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    address = models.TextField()
    landmark = models.CharField(max_length=50)

    def __str__(self):
        return self.name

services_choices = (
       
        ('ECG','ECG'),
        ('BL', 'Blood Examination' ),
        ('UL','Ultrasound') 
        )

class Diagnostics(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    servicesProvided = models.CharField(choices=services_choices, max_length=100)

    def __str__(self):
        return self.name 
