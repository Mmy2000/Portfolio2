# Generated by Django 4.2.8 on 2023-12-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0011_professionalexperience_exp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField(max_length=3000)),
            ],
        ),
    ]
