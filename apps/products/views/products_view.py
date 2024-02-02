
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet, mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.user.models import User
from apps.products.models import Product
from apps.products.serializers import (
    ReadProductSerializer,
    WriteProductSerializer,
    AllowAnyProductSerializer,
    FilteredReadProductSerializer
)
from apps.user.permissions.approved_permission import IsApprovedUser


class ProductsView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Product.objects.all()
    permission_classes = (IsApprovedUser,)
    filter_backends = (
        SearchFilter,
        DjangoFilterBackend
    )

    search_fields = (
        'name',
        'state',
        'categories__name'
    )

    def get_serializer_class(self):
        user: 'User' = self.request.user
        if hasattr(user, 'is_verified') and user.is_verified:
            if self.request.method == 'GET':
                if self.request.GET.get('search', None) is not None:
                    return FilteredReadProductSerializer
                else:
                    return ReadProductSerializer
            else:
                return WriteProductSerializer

        return AllowAnyProductSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = (AllowAny,)

        return super().get_permissions()
