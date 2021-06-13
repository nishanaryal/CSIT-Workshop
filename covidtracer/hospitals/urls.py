from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('datatable', views.datatable, name='Covid19DataTable')
]