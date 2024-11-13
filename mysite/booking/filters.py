from django_filters.rest_framework import FilterSet
from .models import Hotel


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'city': ['exact'],
            'country': ['exact'],
        }