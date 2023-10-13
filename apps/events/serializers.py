from rest_framework import serializers

from apps.events.models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = (

            'id','title', 'description',
            'start_at', 'end_at',
            'location', 'image',
            'price', 'registration',
            'is_active',

        )