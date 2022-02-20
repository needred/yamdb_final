from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Проверка авторства контента - является ли юзер автором.
    """

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or (
            obj.author == request.user
        )


class IsAdminUser(permissions.BasePermission):
    """
    Проверка юзера на права администратора.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.is_admin
        return False


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешения для администратора.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.is_admin
        return False


class IsAuthorOrAdminOrModerator(permissions.BasePermission):
    """
    Разрешения для авторов, администраторов и модераторов.
    """

    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()

        if request.method in ('PATCH', 'DELETE'):
            return (
                obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator
            )

        if request.method in permissions.SAFE_METHODS:
            return True
        return False
