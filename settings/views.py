from django.conf import settings
from django.shortcuts import render
from .models import About , Education , Services ,CategoryService, MySkills  , Summary , ProfessionalExperience
from django.core.mail import send_mail
from django.views.generic import  ListView, DetailView
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post

# Create your views here.
def home(request):
    about = About.objects.last()
    education = Education.objects.all()
    service = Services.objects.all()
    skills = MySkills.objects.all()
    posts = Post.objects.all()
    summary = Summary.objects.last()
    exp = ProfessionalExperience.objects.all()

    return render(request,'home.html', {
        'about':about  , 
        'education':education ,
        'services':service,
        'skills':skills,
        'posts':posts,
        'summary':summary,
        'exp' : exp,
    })