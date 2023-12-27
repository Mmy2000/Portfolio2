import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.urls import reverse
from django.utils import timezone





class About(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=20,null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True)
    headline = models.CharField(max_length=50 , blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True )
    email = models.EmailField( max_length=254, blank=True, null=True)
    resume = models.FileField( upload_to='files/', max_length=100 ,blank=True, null=True)
    about = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    degree = models.CharField( max_length=50 ,blank=True, null=True)

    def __str__(self):
        return str(self.username)
    

class Education(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.CharField(max_length=50 , blank=True, null=True)
    title = models.CharField(max_length=50 , blank=True, null=True)
    subject = models.CharField(max_length=100 , blank=True, null=True)
    university = models.CharField(max_length=100 , blank=True, null=True)
    description = models.TextField(max_length=100000)

    def __str__(self):
        return str(self.user)
    
class Summary(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.CharField(max_length=50 , blank=True, null=True)
    email = models.CharField(max_length=50 , blank=True, null=True)
    phone = models.CharField(max_length=100 , blank=True, null=True)
    address = models.CharField(max_length=100 , blank=True, null=True)
    description = models.TextField(blank=True, null=True , max_length=100000)

    def __str__(self):
        return str(self.user)
    
class  ProfessionalExperience(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    year = models.CharField(max_length=50 , blank=True, null=True)
    title = models.CharField(max_length=50 , blank=True, null=True)
    university = models.CharField(max_length=100 , blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
class EXP(models.Model):
    exp = models.ForeignKey(ProfessionalExperience, related_name="exp", on_delete=models.CASCADE)
    subject = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return str(self.exp)

class Services(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField( null=True,blank=True ,max_length=50)
    category = models.ForeignKey('CategoryService',related_name='service_category',on_delete=models.CASCADE)
    image = models.ImageField(("image"),upload_to='projects/',null=True,blank=True)
    created_at = models.DateTimeField( ("created_at"),default=timezone.now)
    description = models.TextField(("description"),max_length=100000,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)



    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super(Services,self).save(*args,**kwargs)


    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("home:service_detail", kwargs={"slug": self.slug})


class CategoryService(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=100000,null=True,blank=True)
    icons = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Info(models.Model):
    site_name = models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    phone = models.CharField( max_length=30 , null=True, blank=True)
    email = models.EmailField( max_length=254 , null=True, blank=True)
    address = models.CharField( max_length=50 , null=True, blank=True)
    image = models.ImageField(upload_to='users/', null=True, blank=True )
    fb_link = models.URLField( max_length=200)
    twitter_link = models.URLField( max_length=200)
    instagram_link = models.URLField( max_length=200)

    def __str__(self):
        return self.site_name
    

class MySkills(models.Model):
    category = models.ForeignKey('CategorySkills',related_name='skills_category',on_delete=models.CASCADE)
    percent = models.CharField(max_length=30)

    
    def __str__(self):
        return str(self.category)


class CategorySkills(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name