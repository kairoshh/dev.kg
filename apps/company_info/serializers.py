from rest_framework import serializers
from apps.company_info.models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = (
          'id', 'youtube',
          'telegram', 'logo',
          'facebook', 'github',
        )
