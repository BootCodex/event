from django.shortcuts import render
from .models import User, Event, Submission
# Create your views here.


def home_page(request):
    users = User.objects.filter(project_participant=True)
    events = Event.objects.all()
    context = {'user':users, 'events':events}
    return render(request, 'home.html', context)