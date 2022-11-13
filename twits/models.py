from django.conf import settings
from django.db import models
from django.urls import reverse


class Twit(models.Model):
    body = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.body
    
    def get_absolute_url(self):
        return reverse("twit_detail", kwargs={"pk": self.pk})
    


    
