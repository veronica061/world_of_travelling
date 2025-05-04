from django.urls import path

from landing import views

urlpatterns = [
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('services', views.services, name='services'),

]
