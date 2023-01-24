from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

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
    name = models.CharField(max_length=256)
    event_date = models.DateField()
    rsvp = models.ForeignKey(RSVP, on_delete=models.RESTRICT)
    event_poster = models.ImageField(upload_to = "media/img")
    time = models.TimeField(blank=True, null=True)
    venue = models.CharField(max_length=256)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.name

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
        return self.caption


# @receiver(post_save, sender=ContactUs, created)

def SendEmailToContact(sender, instance, created, **kwargs):
    print("created new contact", created)
    print("Sending email to %s" % instance)
    print((instance.email))
 
post_save.connect(SendEmailToContact, sender=ContactUs)


