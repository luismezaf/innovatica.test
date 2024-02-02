from rest_framework.permissions import IsAuthenticated


class IsApprovedUser(IsAuthenticated):
    """
    Allows access only to authenticated and approved users.
    """

    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.is_verified
