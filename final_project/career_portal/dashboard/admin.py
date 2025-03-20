from django.contrib import admin
from .models import (
    Company, 
    JobTag, 
    Job, 
    Event, 
    Resource, 
    Mentor, 
    StudentProfile
)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'logo_code')
    search_fields = ('name', 'location')

@admin.register(JobTag)
class JobTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class JobTagInline(admin.TabularInline):
    model = Job.tags.through
    extra = 1

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_type', 'location', 'date_posted', 'is_active', 'is_featured')
    list_filter = ('job_type', 'is_active', 'is_featured', 'date_posted')
    search_fields = ('title', 'company__name', 'description')
    inlines = [JobTagInline]
    exclude = ('tags',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location', 'is_virtual', 'is_featured')
    list_filter = ('date', 'is_virtual', 'is_featured')
    search_fields = ('title', 'description', 'location')

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource_type', 'is_featured')
    list_filter = ('resource_type', 'is_featured')
    search_fields = ('title', 'description', 'tags')

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'company', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('name', 'title', 'company__name', 'bio', 'expertise')

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'major', 'graduation_year')
    list_filter = ('graduation_year', 'major')
    search_fields = ('user__username', 'user__email', 'major', 'skills', 'interests')