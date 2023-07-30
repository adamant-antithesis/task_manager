from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешаем запросы только на чтение (GET, HEAD, OPTIONS).
        if request.method in permissions.SAFE_METHODS:
            return True

        # При запросах на запись (POST, PUT, DELETE) проверяем, что пользователь - владелец задачи.
        return obj.user == request.user
