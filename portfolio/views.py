from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects': projects})

def profile(request):
    return render(request, 'portfolio/profile.html')

def prodetail(request):
    project = Project.objects.all()
    return render(request, 'portfolio/prodetail.html', {'project'})