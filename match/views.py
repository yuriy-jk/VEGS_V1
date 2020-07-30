from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from account.serializers import UserProfileSerializer
from account.models import UserProfile
from rest_framework.views import APIView
from .models import Match


class MatchView(ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user.id
        queryset = Match.objects.filter(user_id=user)
        result = []
        for match in queryset:
            person_id = match.person
            person_profile = UserProfile.objects.get(user_id=person_id)
            result.append(person_profile)
        return result



