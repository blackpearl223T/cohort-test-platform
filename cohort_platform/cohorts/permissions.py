from rest_framework import permissions

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_teacher

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and not request.user.is_teacher

class IsCohortTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.teacher == request.user

class IsCohortMember(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.members.filter(id=request.user.id).exists()