# Generated by Django 4.0.8 on 2022-11-14 00:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twits', '0002_twit_image_url_alter_twit_image_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_twits', to=settings.AUTH_USER_MODEL),
        ),
    ]
