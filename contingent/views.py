from django.shortcuts import render
from django.http import HttpResponse
from .models import Contingent

# Create your views here.

def contingent(request):
    return render(request, 'contingent.html')    
