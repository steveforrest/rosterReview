# Generated by Django 3.2 on 2022-02-04 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rosterlist',
            name='createdBy',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]