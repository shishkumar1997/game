from django.db import models

# Create your models here.

class Studentdetail(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    