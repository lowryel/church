# Generated by Django 4.1.6 on 2023-03-16 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('churchweb', '0009_alter_events_event_poster_alter_gallery_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='rsvp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='churchweb.rsvp'),
        ),
    ]
