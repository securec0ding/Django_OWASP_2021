from django.urls import path
from . import views

urlpatterns = [
    path('search2/', views.vulnerable_view, name='vulnerable_view'),
]

