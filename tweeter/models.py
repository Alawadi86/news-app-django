from django.db import models


class Twit(models.Model):
    """Twit model"""

    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String"""
        return self.name

    image_ur = models.ImageField()
    # ask about the Varchar

    author = models.ForeignKey(
        "twit",
        on_delete=models.CASCADE,
        related_name="customusers",
    )


class Comment(models.Model):

    """comment model"""

    twit_id = models.ForeignKey(
        "comment",
        on_delete=models.CASCADE,
        related_name="Twit",
    )

    author = models.ForeignKey(
        "comment", on_delete=models.CASCADE, related_name="customuser"
    )


comment = models.CharField(max_length=140)
created = models.DateTimeField(auto_now_add=True)
updated = models.DateTimeField(auto_now=True)

users = models.ManyToManyField(Twit())
""" many to many relationship between users and twits"""
