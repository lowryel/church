# Generated by Django 4.1.6 on 2023-02-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchweb', '0005_randomverse_alter_contactus_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('youtube_link', models.URLField()),
            ],
        ),
    ]