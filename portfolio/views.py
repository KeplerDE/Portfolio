from django.shortcuts import render
from .models import Project


def home(request):
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects': projects})

def profile(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/profile.html', {'projects': projects})

