from django.contrib import admin
from .models import Studentdetail
# Register your models here.

@admin.register(Studentdetail)
class AdminStudent(admin.ModelAdmin):
    list_display = ['id','name','image','created_on','updated_on']