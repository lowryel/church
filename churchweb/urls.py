from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from churchweb.views import *

from django.utils.encoding import iri_to_uri
from urllib.parse import quote

urlpatterns = [
    path('', index, name='index-page'),
    path('church/about', about, name = 'about'),
    path('church/gallery', gallery, name = 'gallery'),
    path('church/events', events, name = 'events' ),
    path('church/give', give, name = 'give'),
    path('church/rsvp/<int:pk>', rsvpView, name='rsvp'),
    path(iri_to_uri("signa/%s" % quote('sig')), signa, name='signa')
]


