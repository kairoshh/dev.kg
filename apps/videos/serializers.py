from rest_framework import serializers

from apps.videos.models import Video

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = (
            'id', 'title',
            'description',
            'create_at', 'preview',
            'video', 'is_active',
        )