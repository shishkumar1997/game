from django.urls import path
from .views import*
urlpatterns = [
    path('api/signup/', UserView,name='signup'),
]