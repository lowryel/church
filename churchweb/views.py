from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from churchweb.models import Fruit, Events, RSVP, Gallery, RecentEvents
from django.db.models import Sum
from .forms import FruitForm, ContactForm
from datetime import date

# Create your views here.


def index(request):
    events_ = Events.objects.all().order_by('-event_date')[:3]
    images = Gallery.objects.all().order_by("-date_posted")[:6]

    for event in events_:
        print(event.rsvp.rs_vp)

    context = {
        'events':events_,
        'images': images,
    }
    return render(request, "index.html", context)


def about(request):
    if request.method == "POST":

        forms = ContactForm(request.POST)
        if forms.is_valid():
            fullname = forms.cleaned_data['fullname']
            email = forms.cleaned_data['email']
            forms.save()
            return redirect('/')
    else:
        forms = ContactForm()
        
    context = {
        'forms': forms,
    }
    return render(request, "about.html", context)

def gallery(request):
    images = Gallery.objects.all()
    name=request.user
    print(name)
    context = {
        'images':images,
    }
    return render(request, 'gallery.html', context)

def events(request):
    rsvp = RSVP.objects.all()
    events_ = Events.objects.filter(status=False).order_by("-event_date")

    recents = RecentEvents.objects.all().order_by("-date")[:2]
    
    context = {
        'events': events_,
        'rsvp':rsvp,
        "recents":recents,
    }

    return render(request, 'events.html', context)


def give(request):

    return render(request, 'give.html')

def rsvpView(request, pk):
    rsvp = RSVP.objects.get(pk=pk)
    context={
        'rsvp': rsvp,
    }
    return render(request, 'rsvp-popup.html', context)

