from django.urls import path

from apps.user.views import UserProfileView

urlpatterns = [
    path('', UserProfileView.as_view(), name='get-user-profile'),
]
