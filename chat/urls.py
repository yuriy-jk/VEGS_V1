from django.urls import path
from .views import CreateChatView, ChatListView, MessageView


urlpatterns = [
    path('create_chat/<int:user_id>', CreateChatView.as_view()),
    path('chats/', ChatListView.as_view()),
    path('chats/<int:chat_id>', MessageView.as_view())
]