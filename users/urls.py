'''Defines url patterns for the users'''

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # include defualt auth urls
    path('', include('django.contrib.auth.urls')),
    # Registartion page
    path('register/', views.register, name = 'register'),
]