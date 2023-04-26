from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from churchweb.models import Events, Gallery, RandomVerse, RecentEvents, RSVP, Sermon
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    events_ = Events.objects.filter(event_type__iexact="major")


    random_verse = RandomVerse.objects.order_by("?").first()
    sermons = Sermon.objects.all()[:5]

    context = {
        'events':events_,
        'verses':random_verse,
        'sermons': sermons,
    }
    return render(request, "index.html", context)

@csrf_exempt
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
    images = Gallery.objects.all().order_by("-date_posted")
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


from django.core.signing import Signer, TimestampSigner
from datetime import timedelta
import logging
def signa(request):
    # logger = logging.dictConfig(__name__)
    # signer = TimestampSigner()
    # value = signer.sign("Hello")
    # unsign = logger.info(signer.unsign(value, max_age=timedelta(5)))
    # return unsign
    # print(value)
    return HttpResponse("Hello There")


