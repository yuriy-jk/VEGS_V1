from django.urls import path

from account.views import UserDetailView, \
    UserProfileCreateView, \
    UserProfileDetailView, \
    UserPreferenceDetailView, \
    UserPreferenceCreateView, \
    UserMediaView

urlpatterns = [
    path('detail/', UserDetailView.as_view(), name='user_detail'),

    path('profile_create/', UserProfileCreateView.as_view(), name='user_profile_create'),
    path('profile/', UserProfileDetailView.as_view(), name='user_profile_update'),

    path('preference_create/', UserPreferenceCreateView.as_view(), name='user_preference_create'),
    path('preference/', UserPreferenceDetailView.as_view(), name='user_preference'),

    path('usermedia/', UserMediaView.as_view(), name='user_media'),
]
