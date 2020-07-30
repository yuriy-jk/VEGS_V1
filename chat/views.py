from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .serializers import ChatSerializer, MessageSerializer
from rest_framework.response import Response

from .models import Chat, Message


class CreateChatView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer

    def get(self, request, user_id):
        user = self.request.user.id
        if not Chat.objects.filter(members__in=[user] and [user_id]):
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
            return Response('ok')
        else:
            message = 'Chat Already exist!'
            return Response(message)


class ChatListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChatSerializer

    def get_queryset(self):
        user = self.request.user.id
        queryset = Chat.objects.filter(members__in=[user])
        return queryset


class MessageView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MessageSerializer

    def post(self, request, chat_id):
        user = self.request.user.id
        chat = chat_id
        body = self.request.POST.get('body')
        new_message = {'user': user,
                       'chat': chat,
                       'body': body}

        serializer = MessageSerializer(data=new_message)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, chat_id):
        messages = Message.objects.filter(chat_id=chat_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)











