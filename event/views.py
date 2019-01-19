from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventForm
from .models import Event
from django.utils import timezone

# Create your views here.
def event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            context=Event.objects.create(**form.cleaned_data)

            return render(request, 'done.html', {'form':context})
    form = EventForm()
    context = {'form':form}
    return render(request, 'event.html', context)

def done(request):
    return render(request, 'done.html')


def display(request):
    obj = Event.objects
    return render(request, 'eventdeets.html', {'obj':obj})
