from account.models import User
from django.db import models


class Like(models.Model):
    owner = models.ForeignKey(User, related_name='like_owner', on_delete=models.CASCADE, db_index=True)
    liked = models.ForeignKey(User, related_name='like_liked', on_delete=models.CASCADE, db_index=True)
