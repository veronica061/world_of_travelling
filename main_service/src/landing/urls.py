from django.urls import path

from landing import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit_review/', views.submit_review, name='submit_review'),

]
