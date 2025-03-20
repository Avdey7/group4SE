from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Job, Event, Resource, Mentor
from .utils.linkedin_api import LinkedInAPI

def dashboard(request):
    """
    Main dashboard view showing featured jobs, events, and resources
    """
    # Get featured jobs
    featured_jobs = Job.objects.filter(is_featured=True, is_active=True)[:3]
    
    # Get upcoming events
    today = timezone.now().date()
    upcoming_events = Event.objects.filter(date__gte=today).order_by('date')[:2]
    
    # Get featured resources
    career_resources = Resource.objects.filter(is_featured=True)[:4]
    
    # Sync with LinkedIn API (commented out until API credentials are available)
    # if request.user.is_authenticated and hasattr(request.user, 'studentprofile'):
    #    profile = request.user.studentprofile
    #    LinkedInAPI.sync_jobs_from_linkedin(
    #        keywords=profile.interests,
    #        location="Charlotte, NC"
    #    )
    
    context = {
        'featured_jobs': featured_jobs,
        'upcoming_events': upcoming_events,
        'career_resources': career_resources,
        'active_tab': 'dashboard',
    }
    
    return render(request, 'dashboard/dashboard.html', context)

def job_board(request):
    """
    View for displaying the job board with filtering options
    """
    jobs = Job.objects.filter(is_active=True)
    
    # Handle filters if provided
    job_type = request.GET.get('job_type')
    location = request.GET.get('location')
    industry = request.GET.get('industry')
    
    if job_type:
        jobs = jobs.filter(job_type=job_type)
    if location:
        jobs = jobs.filter(location__icontains=location)
    
    # Get recommended jobs (would use more sophisticated logic in production)
    recommended_jobs = Job.objects.filter(is_active=True).order_by('?')[:4]
    
    context = {
        'jobs': jobs,
        'job_count': jobs.count(),
        'recommended_jobs': recommended_jobs,
        'active_tab': 'job_board',
    }
    
    return render(request, 'dashboard/job_board.html', context)

def networking_hub(request):
    """
    View for the networking hub page
    """
    featured_mentors = Mentor.objects.filter(is_featured=True)[:4]
    
    # Get upcoming networking events
    today = timezone.now().date()
    networking_events = Event.objects.filter(
        date__gte=today, 
        title__icontains='network'
    ).order_by('date')[:3]
    
    context = {
        'featured_mentors': featured_mentors,
        'networking_events': networking_events,
        'active_tab': 'networking_hub',
    }
    
    return render(request, 'dashboard/networking_hub.html', context)

def mentorship_hub(request):
    """
    View for the mentorship hub page
    """
    mentors = Mentor.objects.all()[:4]
    
    context = {
        'mentors': mentors,
        'active_tab': 'mentorship_hub',
    }
    
    return render(request, 'dashboard/mentorship_hub.html', context)

def resources(request):
    """
    View for displaying career resources
    """
    all_resources = Resource.objects.all().order_by('-id')
    
    context = {
        'resources': all_resources,
        'active_tab': 'resources',
    }
    
    return render(request, 'dashboard/resources.html', context)

@login_required
def profile(request):
    """
    View for user profile and dashboard customization
    """
    # This would include LinkedIn profile integration when implemented
    context = {
        'active_tab': 'profile',
    }
    
    return render(request, 'dashboard/profile.html', context)