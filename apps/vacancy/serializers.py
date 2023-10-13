from rest_framework import serializers

from apps.vacancy.models import Vacancy
from apps.vacancy.models import VacancyDescription

class VacancySerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = (
            'id', 'organization',
            'type_work','typee',
            'is_active',
        )

class VacancyDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacancyDescription
        fields = (
            'id', 'title',
            'description',
            'vacancy',

        )