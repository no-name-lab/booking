from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CheckOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckCRUD(BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_role == 'ownerUser'


class CheckHotelOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class CheckOwnerStatus(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'ownerUser':
            return False
        return True


class CheckRoom(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.room_status == 'свободен':
                return True
        return False


class CheckReview(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user_name


class CheckRoomOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.hotel_room.owner


class CheckBookOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.user_book:
            return True
        return False


class CheckImages(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.room.hotel_room.owner