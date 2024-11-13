from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='user-list')
router.register(r'hotels', HotelListViewSet, basename='hotels-list')
router.register(r'hotels-detail', HotelDetailViewSet, basename='hotels-detail')
router.register(r'rooms', RoomListViewSet, basename='rooms-list')
router.register(r'rooms-detail', RoomDetailViewSet, basename='rooms-detail')
router.register(r'booking', BookingViewSet, basename='booking-list')
router.register(r'reviews', ReviewViewSet, basename='review-list')




urlpatterns = [
    path('', include(router.urls))
]

