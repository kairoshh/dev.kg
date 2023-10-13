from django.db import models

from apps.organizations.models import Organization


class Vacancy(models.Model):
    organization = models.ForeignKey(
        to=Organization, on_delete=models.CASCADE,
        related_name='vacancies'
    )
    type_work = models.CharField(max_length=123)
    salary = models.CharField(max_length=121)
    typee = models.CharField(max_length=123)
    is_active = models.BooleanField(default=False)


class VacancyDescription(models.Model):
    title = models.CharField(max_length=123)
    description = models.TextField()
    vacancy = models.ForeignKey(
        to=Vacancy, on_delete=models.CASCADE,
        related_name='vacancydescriptions'
    )