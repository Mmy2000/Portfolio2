from django.contrib import admin
from . models import About , Resume ,Services , CategoryService ,Info,MySkills,CategorySkills

# Register your models here.
admin.site.register(About)
admin.site.register(Resume)
admin.site.register(Services)
admin.site.register(CategoryService)
admin.site.register(Info)
admin.site.register(MySkills)
admin.site.register(CategorySkills)