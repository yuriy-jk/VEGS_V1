from rest_framework import serializers
from user_media.models import UserMedia


class UserImageSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserMedia
        fields = '__all__'
