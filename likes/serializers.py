from rest_framework import serializers
from account.models import User
from likes.models import Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id',
                  'liked')

