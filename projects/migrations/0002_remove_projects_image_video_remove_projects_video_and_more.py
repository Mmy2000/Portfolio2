# Generated by Django 4.2.8 on 2023-12-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='image_video',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='video',
        ),
        migrations.AddField(
            model_name='projects',
            name='client',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]