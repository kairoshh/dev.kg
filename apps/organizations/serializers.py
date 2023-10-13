from rest_framework import serializers

from apps.organizations.models import Organization

class OrganizationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Organization
        fields = (
            'id', 'name', 
            'description', 'logo',
            'web_site', 'email',
            'phone_number', 'location',
            'user', 'amount'
        )