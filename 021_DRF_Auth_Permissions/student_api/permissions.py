from rest_framework import permissions

class IsAdminorReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user.is_staff)
        
    
class IsAddedByUserorReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user 