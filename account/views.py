from itertools import chain
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, \
    RetrieveUpdateDestroyAPIView, \
    RetrieveUpdateAPIView, get_object_or_404

from user_media.serializers import UserImageSerializer
from .permissions import IsOwnerProfileOrReadOnly

from user_media.models import UserMedia

from account.models import UserProfile, UserPreference
from account.serializers import UserProfileSerializer, \
                                UserPreferenceSerializer, \
                                UserProfileCreateSerializer


class UserProfileCreateView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserPreferenceCreateView(CreateAPIView):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserPreferenceDetailView(RetrieveUpdateAPIView):
    queryset = UserPreference.objects.all()
    serializer_class = UserPreferenceSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class UserDetailView(APIView):

    def get(self, request):
        profile = UserProfile.objects.filter(user=self.request.user)
        preference = UserPreference.objects.filter(user=self.request.user)
        media = UserMedia.objects.filter(user=self.request.user)
        result_list = list(chain(profile.values(
            'user_id', 'first_name', 'last_name', 'is_online', 'birthday',
            'about', 'town', 'food_type', 'gender'
        ),
            preference.values('gender_pref', 'food_type_pref', 'age_pref_min',
                              'age_pref_max', 'distance_pref_min', 'distance_pref_max'),
            media.values('image')))

        return Response(json.dumps(result_list))


class UserMediaView(RetrieveUpdateAPIView):
    queryset = UserMedia.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def perform_update(self, serializer):
        user = self.request.user
        serializer.save(user=user)

