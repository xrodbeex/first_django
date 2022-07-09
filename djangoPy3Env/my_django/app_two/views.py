from django.shortcuts import render, HttpResponse

def second_index(request):
    return HttpResponse("Retrieving information from 2nd app")

# Create your views here.
