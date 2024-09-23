from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    skills = Skill.objects.all() 
    projects = Project.objects.all()
    return render(request, "portfolio_app/home.html", {
        "skills": skills,
        "projects": projects
    })