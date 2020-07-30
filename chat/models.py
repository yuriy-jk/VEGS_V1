from django.db import models
from account.models import User


class Chat(models.Model):
    members = models.ManyToManyField(User, related_name='chat_member')


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='chat_message', on_delete=models.CASCADE, default=False, db_index=True)
    user = models.ForeignKey(User, related_name='user_massage', on_delete=models.CASCADE, db_index=True)
    # reciever = models.ForeignKey(User, related_name='massage_reciever', on_delete=models.CASCADE, db_index=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    is_readed = models.BooleanField(default=False)
    body = models.TextField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.body)
