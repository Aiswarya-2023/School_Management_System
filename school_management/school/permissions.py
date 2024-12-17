from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print(f"User role: {request.user.role}")  # Debugging line
        return request.user.role == 'admin'

    
class IsOfficeStaff(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'office_staff'
    
class IsLibrarian(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'librarian'