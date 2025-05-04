from django.urls import path

from landing import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('registration/', views.registration, name='registration'),
]
