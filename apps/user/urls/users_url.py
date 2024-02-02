from rest_framework.routers import DefaultRouter

from apps.user.views import UserView

router = DefaultRouter()
router.register('', UserView, basename='users')

urlpatterns = router.urls
