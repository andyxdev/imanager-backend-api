from enum import auto
from pickle import TRUE
from django.db import models

# Create your models here.

class Installation(models.Model):
    customer_name = models.CharField(max_length=50,)
    address= models.TextField(max_length=500)
    appointment_date= models.DateField()
    date_created = models.DateTimeField(auto_now_add= True)
    date_modified = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.customer_name

class Status(models.Model):
    STATUS =(
        ('Requested', 'Requested'),
        ('In progress','In progress'),
        ('Complete','Complete'),
        ('Rejected','Rejected'),
    )
    installation = models.ForeignKey(Installation, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, null =True, choices= STATUS)
    notes = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.status
