# Generated by Django 5.2 on 2025-05-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_application_applied_at_application_cover_letter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseekerprofile',
            name='experience',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='jobseekerprofile',
            name='skills',
            field=models.TextField(default=''),
        ),
    ]
