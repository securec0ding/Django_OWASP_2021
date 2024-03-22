from django.urls import path
from . import views

urlpatterns = [
    path('transfer/', views.vulnerable_transfer, name='vulnerable_transfer'),
]

