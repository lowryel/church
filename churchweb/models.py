from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.conf import settings


# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class RSVP(models.Model):
    rs_vp = models.CharField(max_length=120)
    designation = models.CharField(max_length=120, blank=True, null=True)
    contact = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = _("RSVP")
        verbose_name_plural = _("RSVP")
    def __str__(self):
        return self.designation + " " + self.rs_vp

class Events(models.Model):
    STATUS_CHOICE = (
        ("normal", "N"),
        ("major", "M")
    )
    name = models.CharField(max_length=256)
    event_type=models.CharField(choices=STATUS_CHOICE, max_length=120, default="N")
    event_date = models.DateField()
    rsvp = models.ForeignKey(RSVP, on_delete=models.RESTRICT)
    event_poster = models.ImageField(upload_to = "media/img")
    time = models.TimeField(blank=True, null=True)
    from_time = models.TimeField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)

    venue = models.CharField(max_length=256)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name

class Sermon(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    youtube_link=models.URLField(max_length=200)

    def __str__(self):
        return self.title

class RecentEvents(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    event_details = models.TextField()
    image = models.ImageField(upload_to = "media/img")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Recent Event")
        verbose_name_plural = _("Recent Events")

    def __str__(self):
        return self.event.name

defaultVerse = "I and my father are one - John 10:30"
class RandomVerse(models.Model):
    verse = models.TextField(default=defaultVerse)

class ContactUs(models.Model):
    fullname = models.CharField(max_length=256)
    email = models.EmailField(null= True)
    phone = models.PositiveIntegerField(null=True)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        verbose_name = _("Contact Us")
        verbose_name_plural = _("Contact Us")

    def __str__(self):
        return self.fullname


class Gallery(models.Model):
    caption = models.CharField(max_length=128, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = _("Gallery")
        verbose_name_plural = _("Gallery")

    def __str__(self):
        return "media"


# @receiver(post_save, sender=ContactUs, created)

def SendEmailToContact(sender, instance, created, **kwargs):
    print("created new contact", created)
    print("Sending email to %s" % instance)
    print((instance.email))
    try:
        if created:
            send_mail(
                f'Hello {instance.fullname}',
                'We welcome you to Coffie Bekoe Ministry (Easy wrapper for sending a single message to a recipient list. All members of the recipient list will see the other recipients in the field.)',
                settings.EMAIL_HOST_USER,
                [instance.email],
                fail_silently = False,
            )
    except Exception:
        return None
 
post_save.connect(SendEmailToContact, sender=ContactUs)

# zqvpkhupxvcwbkrq
