# Generated by Django 4.2.8 on 2023-12-27 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('image', models.ImageField(upload_to='post/', verbose_name='image')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('description', models.TextField(max_length=100000, verbose_name='description')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_auther', to=settings.AUTH_USER_MODEL, verbose_name='auther')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
            ],
        ),
    ]
