from django.contrib import admin

# Register your models here.
from django.contrib import admin
from user_media.models import UserMedia

# Register your models here.


@admin.register(UserMedia)
class UserMediaAdmin(admin.ModelAdmin):
    list_display = [
        'image_tag',
        'user',
        'id',
        'is_main',

    ]

