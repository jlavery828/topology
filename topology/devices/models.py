
from django.db import models
from django.db.models import Model 

# Create your models here.
class Switch(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    description = models.TextField(blank=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)


    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    description = models.TextField(blank=True)
    mac_address = models.CharField(max_length=17, blank=True, null=True)
    parent_device = models.ForeignKey(Switch, null=True, blank=True, on_delete=models.SET_NULL)
    vlan = models.IntegerField()


    def __str__(self):
        return self.name
