from django.db import models


class Post(models.Model):
    # attributes for each post that we will collect
    objects = None
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    # A slug is a short label for something, containing only letters, numbers, underscores or hyphens.They're
    # generally used in URLs
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
