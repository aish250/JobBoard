# jobs/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, Application, JobSeekerProfile
from .forms import ApplicationForm, JobSeekerProfileForm

def home(request):
    """Home page view"""
    return render(request, 'jobs/home.html')

def job_list(request):
    """List all available jobs"""
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/list.html', {'jobs': jobs})

@login_required
def job_detail(request, pk):
    """Job detail view with application form"""
    job = get_object_or_404(Job, pk=pk)
    
    try:
        profile = request.user.jobseekerprofile
        has_profile = True
    except JobSeekerProfile.DoesNotExist:
        profile = None
        has_profile = False
    
    if request.method == 'POST':
        if not has_profile:
            messages.error(request, "You need to create a Job Seeker profile before applying")
            return redirect('job_detail', pk=pk)
            
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = profile
            application.save()
            messages.success(request, "Application submitted successfully!")
            return redirect('job_list')
    else:
        form = ApplicationForm()
    
    context = {
        'job': job,
        'form': form,
        'has_profile': has_profile
    }
    return render(request, 'jobs/detail.html', context)

@login_required
def create_profile(request):
    """View for creating a job seeker profile"""
    if hasattr(request.user, 'jobseekerprofile'):
        return redirect('job_list')
        
    if request.method == 'POST':
        form = JobSeekerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Profile created successfully!")
            return redirect('job_list')
    else:
        form = JobSeekerProfileForm()
    
    return render(request, 'jobs/create_profile.html', {'form': form})