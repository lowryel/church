from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from churchweb.views import *

urlpatterns = [
    path('', index, name='index-page'),
    path('church/about', about, name = 'about'),
    path('church/gallery', gallery, name = 'gallery'),
    path('church/events', events, name = 'events' ),
    path('church/give', give, name = 'give')
]


