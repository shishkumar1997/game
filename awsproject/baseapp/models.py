from django.db import models

# Create your models here.

class Studentdetail(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    is_deleted = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        db_table = 'student_information'
        indexes = [models.Index(fields=['name'])]
