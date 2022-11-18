from django.conf import settings
from django.db import models
from django.urls import reverse




class Twit(models.Model):
    body = models.TextField()
    upload_path = 'media/twit'
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.image_url:
            import urllib, os
            from urlparse import urlparse
            filename = urlparse(self.image_url).path.split('/')[-1]
            urllib.urlretrieve(self.image_url, os.path.join(file_save_dir, filename))
            self.image = os.path.join(upload_path, filename)
            self.image_url = ''
            super(Product, self).save()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE,
    )
    likes =  models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_twits",
        blank = True,
    )

    def __str__(self):
        """ Twet strings """
        return self.body
    
    def get_absolute_url(self):
        return reverse("twit_detail", kwargs={"pk": self.pk})


    def get_like_url(self):
        """ get like url based on pk """
        return reverse("twit_like", kwargs={"pk": self.pk})
        

    


class Comment(models.Model):
    twit = models.ForeignKey(
        Twit, on_delete= models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
     on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("twit_list")
    


        
    


    
