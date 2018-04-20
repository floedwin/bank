from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class Post(models.Model):
    post = models.CharField(max_length=200)
    user = models.ForeignKey(User)

class Registercustomer(models.Model):
    First_name = models.CharField(max_length=200, default='')
    Last_name = models.CharField(max_length=200, default='')
    Email = models.EmailField(blank=True)
    Contact = models.IntegerField(default=0)
    Residence = models.CharField(max_length=200, default='')
    Next_of_kin = models.CharField(max_length=200, default='')
    Occupation = models.CharField(max_length=200, default='')
    Relationship = models.CharField(max_length=200, default='')
    Next_of_kin = models.CharField(max_length=200, default='')
    Relationship = models.CharField(max_length=200, default='')


    def __str__(self):
        return self.First_name

class CustomerBankaccount(models.Model):
    Full_name = models.CharField(max_length=200, default='')
    Email = models.EmailField(blank=True)
    Contact = models.IntegerField(default=0)
    Residence = models.CharField(max_length=200, default='')
    Work_history = models.CharField(max_length=200, default='')
    Identification_information = models.IntegerField(default=0)
    Next_of_kin = models.CharField(max_length=200, default='')
    Relationship = models.CharField(max_length=200, default='')
    Account_number = models.IntegerField(default=0)
    def __str__(self):
        return self.Full_name

class Registercustomertranscations(models.Model):
    Full_name = models.CharField(max_length=200, default='')
    Email = models.EmailField(blank=True)
    Contact = models.IntegerField(default=0)
    Account_number = models.IntegerField(default=0)
    Transcation_type = models.CharField(max_length=200, default='')
    Amount = models.IntegerField(default=0)
    Transcation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.Full_name


def __unicode__(self):
    return self.First_name




