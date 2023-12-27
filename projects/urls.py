from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('' , views.ProjectList.as_view() , name='project_list'),
    path('<slug:slug>' , views.ProjectDetail.as_view() , name='project_detail'),
    path('category/<str:slug>' , views.ProjectByCategory.as_view() , name='project_by_category'),
    path('tags/<str:slug>' , views.ProjectByTags.as_view() , name='project_by_tags'),
]