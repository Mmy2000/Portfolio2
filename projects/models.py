from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify 


# Create your models here.
class Projects(models.Model):
    auther = models.ForeignKey(User, related_name="project_auther",verbose_name=('auther'), on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name=('title'))
    tags = TaggableManager(("tags"))
    image = models.ImageField(("image"),upload_to='projects/')
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    description = models.TextField(("description"),max_length=100000)
    categoryproject = models.ForeignKey('CategoryProject',related_name='project_category',verbose_name=('categoryproject'),on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    url = models.CharField(null=True,blank=True, max_length=50)
    client = models.CharField(null=True,blank=True, max_length=50)


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Projects,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("projects:project_detail", kwargs={"slug": self.slug})

class CategoryProject(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    
class ImageProject(models.Model):
    project = models.ForeignKey(Projects,related_name='project_image',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projectimages/')

    def __str__(self):
        return str(self.project)