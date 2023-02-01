from django.contrib import admin
from churchweb.models import Events, RSVP, ContactUs, RecentEvents, Gallery, RandomVerse

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
    list_display = ['fullname', 'email', 'phone']

