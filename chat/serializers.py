from rest_framework import serializers
from chat.models import Message, Chat

from account.models import User


class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = ('id',
                  'members')


class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = ('id',
                  'chat',
                  'user',
                  'created',
                  'is_readed',
                  'body')



