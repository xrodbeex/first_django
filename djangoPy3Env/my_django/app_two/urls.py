from django.urls import path
from . import views

urlpatterns = [
    path('second-index', views.second_index),
]