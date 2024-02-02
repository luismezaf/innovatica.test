from rest_framework.routers import DefaultRouter

from apps.products.views import ProductsView, ProductCategoryView

router = DefaultRouter()
router.register('categories', ProductCategoryView, basename='get-product-categories')
router.register('', ProductsView, basename='get-products')

urlpatterns = router.urls
