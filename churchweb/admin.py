from django.contrib import admin
from churchweb.models import Events, RSVP, ContactUs, RecentEvents, Gallery, RandomVerse, Sermon

# Register your models here.

# admin.site.register(Fruit)

class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_date', 'venue', 'status']

admin.site.register(Events, EventsAdmin)
admin.site.register(RSVP)
# admin.site.register(ContactUs)
admin.site.register(RecentEvents)
admin.site.register(Gallery)

admin.site.register(RandomVerse)
@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'phone', 'time']


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ['title', 'youtube_link']
    list_display_links = ['youtube_link']
    list_editable = ['title']

    
