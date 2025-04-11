from rest_framework.permissions import BasePermission


class IsAlireza(BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.username == 'alireza':
            return True
        else:
            return False