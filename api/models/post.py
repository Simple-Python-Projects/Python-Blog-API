from django.db import models
from api.models import Category


class Post(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.CharField(max_length=200, blank=False, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']
