from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Post , PostCategory
from taggit.models import Tag
from django.db.models import Count
from django.db.models.query_utils import Q
# Create your views here.


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = PostCategory.objects.all().annotate(post_count=Count('post_category'))
        context["tags"] = Tag.objects.all()
        context["recent_posts"] = Post.objects.all()[:3]
        return context