from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = obj.user == request.user
        print('PERMISSIONS: IsOwnerOrReadOnly://', is_owner)
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return is_owner


class IsSuperUserOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_superuser = request.user.is_superuser
        print('PERMISSIONS: IsSuperUserOwnerOrReadOnly://', is_superuser)
        check_is_authenticated_superuser = obj.user == request.user and is_superuser
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return check_is_authenticated_superuser


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        is_superuser = request.user.is_superuser
        print('PERMISSIONS: IsSuperUserOrReadOnly://', is_superuser)
        check_is_authenticated_superuser = request.user is not None and is_superuser
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return check_is_authenticated_superuser


class IsStaffOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        is_staff = request.user.is_staff
        print('PERMISSIONS: IsStaffOwnerOrReadOnly://', is_staff)
        check_is_authenticated_staff = obj.user == request.user and is_staff

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return check_is_authenticated_staff


class IsStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        is_staff = request.user.is_staff
        print('PERMISSIONS: IsStaffOrReadOnly:// test', request.user is not None and is_staff)
        check_is_authenticated_staff = request.user is not None and is_staff

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return check_is_authenticated_staff
