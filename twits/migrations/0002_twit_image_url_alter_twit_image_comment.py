# Generated by Django 4.0.8 on 2022-11-13 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('twits', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twit',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='twit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/twit'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=140)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('twit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twits.twit')),
            ],
        ),
    ]
