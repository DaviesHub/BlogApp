from django.db import models

# Create your models here.
# Models describe what data you want to store

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField(blank=True)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
