from django.contrib import admin
from account.models import User, UserProfile, UserPreference
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'is_staff',
        'is_active',
        'date_joined',
    ]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'first_name',
        'last_name',
        'food_type',
        'gender',
        'is_online',
        'birthday',
        'about',
        'town'
    ]


@admin.register(UserPreference)
class UserPreference(admin.ModelAdmin):
    list_display = [
        'user',
        'gender_pref',
        'food_type_pref',
        'age_pref_min',
        'age_pref_max',
        'distance_pref_min',
        'distance_pref_max'
    ]
