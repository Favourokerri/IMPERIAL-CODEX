from django.contrib import admin
from django.urls import path, include
from base import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('courses/', views.courses, name="courses"),
    path('attendance/', views.attendance, name="attendance"),
    path('enroll/', views.enroll, name="enroll"),
    path('services/', views.services, name="services"),
    
]