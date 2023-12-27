from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Projects , CategoryProject
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q



class ProjectList(ListView):
    model = Projects
    paginate_by = 12
    def get_queryset(self) :
        name = self.request.GET.get('q','')
        object_list = Projects.objects.filter(
            Q(title__icontains = name) |
            Q(description__icontains = name)
        )
        return object_list
    
class ProjectDetail(DetailView):
    model = Projects

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = CategoryProject.objects.all().annotate(project_count=Count('project_category'))
        context["tags"] = Tag.objects.all()
        context["recent_project"] = Projects.objects.all()[:3]
        return context
    
class ProjectByCategory(ListView):
    model = Projects


    def get_queryset(self) :
        slug = self.kwargs['slug']
        object_list = Projects.objects.filter(
            Q(categoryproject__name__icontains = slug)
        )
        return object_list
    
class ProjectByTags(ListView):
    model = Projects

    def get_queryset(self) :
        slug = self.kwargs['slug']
        object_list = Projects.objects.filter(
            Q(tags__name__icontains = slug)
        )
        return object_list