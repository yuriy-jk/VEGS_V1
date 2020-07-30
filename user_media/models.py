from django.db import models
from account.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
import account.models


class UserMedia(models.Model):
    user = models.ForeignKey(User, related_name='user_media', on_delete=models.CASCADE, db_index=True)
    image1 = models.ImageField(blank=True, upload_to='user_photo')
    image2 = models.ImageField(blank=True, upload_to='user_photo')
    image3 = models.ImageField(blank=True, upload_to='user_photo')
    image4 = models.ImageField(blank=True, upload_to='user_photo')
    image5 = models.ImageField(blank=True, upload_to='user_photo')
    image6 = models.ImageField(blank=True, upload_to='user_photo')
    image7 = models.ImageField(blank=True, upload_to='user_photo')
    image8 = models.ImageField(blank=True, upload_to='user_photo')
    image9 = models.ImageField(blank=True, upload_to='user_photo')

    is_main = models.BooleanField(default=False)

    @property
    def image_tag(self):
        return mark_safe('<img width="150" src="%s" />' % self.image1.url)
