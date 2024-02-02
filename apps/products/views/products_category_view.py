
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet, mixins

from apps.products.models import ProductCategory
from apps.products.serializers import ProductCategorySerializer
from apps.user.permissions.approved_permission import IsApprovedUser


class ProductCategoryView(
    GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    queryset = ProductCategory.objects.all()
    permission_classes = (IsApprovedUser,)
    serializer_class = ProductCategorySerializer

    def get_permissions(self):
        if self.request.method == 'get':
            self.permission_classes = (AllowAny,)

        return super().get_permissions()
