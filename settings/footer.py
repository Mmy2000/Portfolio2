from .models import Info , Services , CategoryService , About
from django.db.models import Count
from django.views.generic import  ListView
from django.db.models.query_utils import Q



def myfooter(request):
    myfooter = Info.objects.last()
    about = About.objects.last()
    context = {
        'myfooter':myfooter , 
        'abouts' : about,
    }
    return context

