
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import GenericViewSet, mixins

from apps.user.serializers import UserSerializer, ResetPasswordSerializer
from apps.user.models import User


class UserView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

    @action(detail=True, methods=['post'])
    def reset_password(self, request: HttpRequest, pk: str = None):
        """
        Expects two fields in data:
        - password
        - confirm_password
        Both of them must have the same value.
        """

        data: dict = request.data
        serializer = ResetPasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user: 'User' = self.get_object()
        user.set_password(data.get('password'))
        user.save()
        return Response()

    @action(detail=True, methods=['post'])
    def approve(self, request: HttpRequest, pk: str = None):
        """
        Approve users by id
        """

        user: 'User' = self.get_object()

        # Validate already approved
        if user.is_verified:
            raise ValidationError({"error": "Account already approved."})

        # Approve user account
        user.is_verified = True
        user.save()
        return Response({"status": "approved"})
