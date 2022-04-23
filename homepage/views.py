from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bio, Project

# Create your views here.
def home(request):
    details = Bio.objects.all()
    projects = Project.objects.all()

    context = {
        'details': details,
        'projects': projects
    }
    return render(request, 'homepage/index.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'homepage/project_home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.all().order_by('-date')

class ProjectDetailView(DetailView):
    model = Project

def about(request):
    details = Bio.objects.all()

    context = {
        'details': details
    }

    return render(request, 'homepage/about.html', context)

def resume(request):
    return render(request, 'homepage/resume.html')