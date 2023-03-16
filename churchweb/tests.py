from django.test import TestCase
from churchweb.models import Events, Gallery, RandomVerse, RecentEvents, RSVP, Sermon
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.index_url = reverse('index-page')
        self.about_url = reverse('about')
        self.gallery_url = reverse('gallery')
        self.events_url = reverse('events')
        self.give_url = reverse('give')

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_about_view(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_gallery_view(self):
        response = self.client.get(self.gallery_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_events_view(self):
        response = self.client.get(self.events_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'events.html')

    def test_give_view(self):
        response = self.client.get(self.give_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'give.html')



# Create your tests here.
