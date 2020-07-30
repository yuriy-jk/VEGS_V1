from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from user_media.models import UserMedia
from user_media.serializers import UserImageSerializer
from rest_framework.parsers import MultiPartParser


class AddImageView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = UserMedia.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
