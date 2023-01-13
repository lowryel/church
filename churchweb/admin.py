from django.contrib import admin
from churchweb.models import Fruit, Events, RSVP, ContactUs, RecentEvents, Gallery

# Register your models here.

admin.site.register(Fruit)

class EventsAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_date', 'venue', 'status']

admin.site.register(Events, EventsAdmin)
admin.site.register(RSVP)
admin.site.register(ContactUs)
admin.site.register(RecentEvents)
admin.site.register(Gallery)


