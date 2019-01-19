from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, 'index.html')

def done(request):
    name = request.GET['Name']
    phone = request.GET['Phone']
    college = request.GET['College']
    email = request.GET['Email']
    return render(request, 'done.html')
