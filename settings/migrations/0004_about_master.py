# Generated by Django 4.2.8 on 2023-12-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_about_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='master',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]