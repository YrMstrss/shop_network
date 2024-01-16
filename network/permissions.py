from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Проверка активности сотрудника
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_active
