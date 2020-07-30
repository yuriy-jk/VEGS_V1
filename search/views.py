from rest_framework.generics import ListAPIView

from account.models import UserProfile, UserPreference
from user_media.models import UserMedia
from account.serializers import UserProfileSerializer

from rest_framework.permissions import IsAuthenticated

#from VEGS_V1.paginator import CustomPagination


class UserSearchListView(ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    #pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        pref = UserPreference.objects.filter(user=user)
        gender = pref.values_list().get()[2]
        food = pref.values_list().get()[3]
        min_age = pref.values_list().get()[4]
        max_age = pref.values_list().get()[5]
        queryset = UserProfile.objects.filter(gender=gender,).filter(food_type=food)
        result = [x for x in queryset if min_age <= x.age <= max_age]
        return result
