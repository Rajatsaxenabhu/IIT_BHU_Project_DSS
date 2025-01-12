from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('demo/',views.demo,name='demo'),
    path('result/',views.get_selected_columns,name='result')
]
