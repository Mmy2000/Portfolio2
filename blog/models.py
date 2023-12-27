from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.utils.text import slugify 



class Post(models.Model):
    auther = models.ForeignKey(User, related_name="post_auther",verbose_name=('auther'), on_delete=models.CASCADE)
    title = models.CharField(max_length=100,verbose_name=('title'))
    tags = TaggableManager(("tags"))
    image = models.ImageField(("image"),upload_to='post/')
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    description = models.TextField(("description"),max_length=100000)
    slug = models.SlugField(null=True,blank=True)
    category = models.ForeignKey('PostCategory',related_name='post_category',verbose_name=('category'),on_delete=models.CASCADE ,null=True,blank=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Post,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

class PostImages(models.Model):
    post = models.ForeignKey(Post, related_name='post_image', on_delete=models.CASCADE)
    image = models.ImageField( upload_to='postImages')

    def __str__(self):
        return str(self.post.title)
    
class PostCategory(models.Model):
    name = models.CharField(null=True,blank=True, max_length=50)

    def __str__(self):
        return self.name