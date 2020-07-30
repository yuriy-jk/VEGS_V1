from django.db import models
from account.models import User


class Match(models.Model):
    user = models.ForeignKey(User, related_name='user_match', on_delete=models.CASCADE, db_index=True)
    person = models.PositiveIntegerField(db_index=True)



