from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContingentForm
from .models import Contingent
# Create your views here.
def contingent(request):
    form = ContingentForm()
    if request.method == "POST":
        form = ContingentForm(request.POST)
        if form.is_valid():
            valid = Contingent.objects.create(**form.cleaned_data)
            return render(request,'codone.html',{'form':valid})

    form = ContingentForm()

    context = {'form':form}
    return render(request, 'contingent.html', context)


def display(request):
    obj = Contingent.objects
    return render(request, 'contdeets.html', {'obj':obj})

def done(request):
    return render(request,'codone.html')
