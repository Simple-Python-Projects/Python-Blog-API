from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdAt']
