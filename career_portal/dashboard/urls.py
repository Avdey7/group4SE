from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('jobs/', views.job_board, name='job_board'),
    path('networking/', views.networking_hub, name='networking_hub'),
    path('mentorship/', views.mentorship_hub, name='mentorship_hub'),
    path('resources/', views.resources, name='resources'),
    path('profile/', views.profile, name='profile'),
]