from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo_code = models.CharField(max_length=10, help_text="Short code for logo placeholder (e.g., 'DB' for Digital Bank)")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Companies"

class JobTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('internship', 'Internship'),
        ('co-op', 'Co-op'),
        ('contract', 'Contract'),
    ]
    
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=100)
    description = models.TextField()
    salary_range = models.CharField(max_length=50, blank=True, null=True)
    tags = models.ManyToManyField(JobTag)
    date_posted = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    linkedin_job_id = models.CharField(max_length=100, blank=True, null=True, help_text="ID from LinkedIn API")
    
    def __str__(self):
        return f"{self.title} at {self.company.name}"
    
    class Meta:
        ordering = ['-date_posted']

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    is_virtual = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date', 'time']

class Resource(models.Model):
    RESOURCE_TYPE_CHOICES = [
        ('guide', 'Guide'),
        ('tool', 'Tool'),
        ('template', 'Template'),
        ('assessment', 'Assessment'),
        ('video', 'Video'),
        ('article', 'Article'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPE_CHOICES)
    url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, help_text="Comma-separated tags")
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    bio = models.TextField()
    expertise = models.CharField(max_length=200, help_text="Comma-separated areas of expertise")
    photo = models.ImageField(upload_to='mentor_photos/', blank=True, null=True)
    initials = models.CharField(max_length=2, help_text="Initials for photo placeholder")
    linkedin_profile = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    skills = models.TextField(blank=True, help_text="Comma-separated skills")
    interests = models.TextField(blank=True, help_text="Comma-separated career interests")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    linkedin_id = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username