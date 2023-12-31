from django.shortcuts import render
from .models import User, Event, Submission
# Create your views here.


def home_page(request):
    users = User.objects.filter(project_participant=True)
    events = Event.objects.all()
    context = {'users':users, 'events':events}
    return render(request, 'home.html', context)


def event_page(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request, 'event.html', context)



def reg_confirmation(request, pk):
    event = Event.objects.get(id=pk)
    context = {'event':event}
    return render(request, 'event_confirmation.html', context)