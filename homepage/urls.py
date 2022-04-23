from django.urls import path
from .views import ProjectListView, ProjectDetailView
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('projects/', ProjectListView.as_view(), name='projects-home'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
]