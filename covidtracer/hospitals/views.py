from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to the CSIT Axure Workhop\'s Homepage!', content_type='text/plain')


def datatable(request):
    return HttpResponse('List of All Hospitals in Kathmandu', content_type='text/plain')