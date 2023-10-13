from django.db import models



class Company(models.Model):
    telegram = models.URLField()
    logo = models.ImageField(upload_to='post/images')
    youtube = models.URLField()
    facebook = models.URLField()
    github = models.URLField()