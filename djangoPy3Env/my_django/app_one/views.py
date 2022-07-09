from django.shortcuts import render, HttpResponse

# Create your views here.
def first_index(request):
    return HttpResponse("Retrieving information from 1st app")