
from django.contrib import admin
from django.urls import path
from baseapp import views

urlpatterns = [
    path('student/', views.StudentdetailAPI().as_view()),
    path('student/<int:id>/', views.StudentdetailAPI().as_view()),
]