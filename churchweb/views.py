from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from churchweb.models import Fruit, Events, RSVP, Gallery, RecentEvents, RandomVerse, Sermon
from django.db.models import Sum
from .forms import FruitForm, ContactForm
from datetime import date

# Create your views here.


def index(request):
    events_ = Events.objects.all().exclude(event_type="N")

    random_verse = RandomVerse.objects.order_by("?").first()
    sermons = Sermon.objects.all()

    context = {
        'events':events_,
        'verses':random_verse,
        'sermons': sermons,
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

# gallery view
def gallery(request):
    images = Gallery.objects.all()
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
        # 'rsvp':rsvp,
        "recents":recents,
    }
    return render(request, 'events.html', context)


def give(request):

    return render(request, 'give.html')


def rsvpView(request, pk):
    events_ = Events.objects.get(pk=pk)
    print(events_.id)

    context={
        'event': events_,
    }
    return render(request, 'rsvp-popup.html', context)

