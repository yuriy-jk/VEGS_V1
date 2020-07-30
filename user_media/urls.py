from django.urls import path
from user_media.views import AddImageView

urlpatterns = [
    path('add_image/', AddImageView.as_view())
]
