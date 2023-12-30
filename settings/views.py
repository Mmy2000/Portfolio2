from django.conf import settings
from django.shortcuts import render , redirect
from .models import About , Education , Services ,CategoryService, MySkills  , Summary , ProfessionalExperience
from django.core.mail import send_mail
from django.views.generic import  ListView, DetailView
from django.db.models.query_utils import Q
from django.db.models import Count
from blog.models import Post
from projects.models import Projects
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def home(request):
    about = About.objects.last()
    education = Education.objects.all()
    service = Services.objects.all()
    skills = MySkills.objects.all()
    posts = Post.objects.all()
    summary = Summary.objects.last()
    exp = ProfessionalExperience.objects.all()
    projects = Projects.objects.all()
    project_count = projects.count() 
    awards = project_count+2
    about.views += 1
    about.save()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid(): 
            form.save()
            subject = "Welcome , Airbnb with you. "
            message = "Our team will contact you within 24hrs."
            email_from = settings.EMAIL_HOST_USER
            email = form.cleaned_data['email']
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list])
            messages.success(request, 'Your message has been send')
            return redirect(reverse('settings:contact'))
    form = ContactForm()

    return render(request,'home.html', {
        'about':about  , 
        'education':education ,
        'services':service,
        'skills':skills,
        'posts':posts,
        'summary':summary,
        'exp' : exp,
        'projects':projects,
        'form':form,
        'awards':awards,
        'project_count':project_count
    })

