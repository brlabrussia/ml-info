import rest_framework_filters as filters
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import viewsets

from banks.models import Rating
from banks.serializers import RatingSerializer


class RatingFilter(filters.FilterSet):
    class Meta:
        model = Rating
        fields = {
            'created_at': '__all__',
            'updated_at': '__all__',
        }


class RatingViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
    ordering = ['-updated_at']
    filterset_class = RatingFilter
