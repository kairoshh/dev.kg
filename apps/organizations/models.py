from django.db import models

from rest_framework.decorators import action

from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    name = models.CharField(max_length=123)
    description = models.TextField()
    logo = models.ImageField(upload_to='post/images')
    web_site = models.URLField(max_length=123)
    email = models.EmailField(max_length=123)
    phone_number = models.CharField(max_length=123)
    location = models.CharField(max_length=123)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name='organizations'
    )

    @property
    def amount(self):
        return self.vacancies.count()
