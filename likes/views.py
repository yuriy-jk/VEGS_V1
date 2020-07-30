from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from likes.serializers import LikeSerializer
from likes.models import Like
from match.models import Match


class LikeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        owner = self.request.user.id
        liked = pk
        Like.objects.create(owner_id=owner, liked_id=liked)
        try:
            queryset = Like.objects.filter(owner=liked)
            match = [x for x in queryset if x.liked_id == owner]
            if match:
                Match.objects.create(user_id=owner, person=liked)
                Match.objects.create(user_id=liked, person=owner)

                massage = 'You got match!'
                return Response(massage)
            else:
                return Response("Not match!")
        except:
            pass

