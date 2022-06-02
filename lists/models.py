from django.db import models

# Create your models here.
#List must be defined before Item
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List,on_delete=models.CASCADE,default=None)

