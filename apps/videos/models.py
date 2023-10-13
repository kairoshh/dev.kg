from django.db import models

from apps.organizations.models import Organization

class Video(models.Model):
    organization = models.ForeignKey(
        to=Organization, on_delete=models.CASCADE,
        related_name='videos'
    )
    title = models.CharField(max_length=123)
    create_at = models.DateField(auto_now_add=True)
    description = models.TextField()
    preview = models.ImageField(upload_to='post/images')
    video = models.URLField(max_length=123)
    is_active = models.BooleanField()
