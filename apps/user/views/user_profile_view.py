from django.http import HttpRequest
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.user.serializers import UserSerializer


class UserProfileView(APIView):

    def get(self, request: HttpRequest):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(serializer.data)
