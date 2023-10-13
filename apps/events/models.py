from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=124)
    description = models.TextField()
    start_at = models.DateTimeField(auto_now_add=True)
    end_at  = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=124)
    image = models.ImageField(upload_to='post/images')
    price = models.PositiveIntegerField(default=0)
    registration = models.URLField(max_length=123)
    is_active = models.BooleanField(default=False)