from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("services", views.services, name='services'),
    path("contactus", views.contactus, name='contactsus')


]
