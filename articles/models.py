from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return f'{self.body[:50]}...'

    # def get_absolute_url(self):
    #     return reverse("articles:article-detail", kwargs = { "slug": self.slug })
