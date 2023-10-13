from django.contrib import admin

from apps.vacancy.models import Vacancy, VacancyDescription

admin.site.register(Vacancy)
admin.site.register(VacancyDescription)
