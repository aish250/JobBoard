# jobs/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    company_description = models.TextField()

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', blank=True)
    skills = models.TextField(default="")
    experience = models.TextField(default="")
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('FULL', 'Full-time'),
        ('PART', 'Part-time'),
        ('REMOTE', 'Remote'),
    ]
    
    employer = models.ForeignKey(EmployerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(JobSeekerProfile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)

    cover_letter = models.TextField(null=True, blank=True)

    status = models.CharField(max_length=20, default='pending')
    applied_at = models.DateTimeField(default=timezone.now)