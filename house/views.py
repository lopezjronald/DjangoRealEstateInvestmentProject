from django.shortcuts import render
from .models import Project

def house(request):
    projects = Project.objects.all()
    return render(request, 'house/home.html', {'projects': projects})
