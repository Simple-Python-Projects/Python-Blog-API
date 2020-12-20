from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.CharField(max_length=200, blank=False, unique=True, null=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']
