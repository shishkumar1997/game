
from django.contrib import admin
from django.urls import path
from baseapp import views

urlpatterns = [
    path('api/get_student/', views.StudentdetailAPI().as_view(),name='get_student'),
    path('api/get_student/<int:id>/', views.StudentdetailAPI().as_view(),name='get_student'),
    path('api/post_student/', views.AddStudentdetailAPI().as_view(),name='post_student'),
    path('api/edit_student/', views.UpdateStudentdetailAPI().as_view(),name='edit_student'),
    path('api/edit1_student/', views.Update1StudentdetailAPI().as_view(),name='edit1_student'),
    path('api/delete_student/', views.DeleteStudentdetailAPI().as_view(),name='delete_student'),
    path('api/student_login/', views.StudentLoginAPIView().as_view(),name='student_login'),
]