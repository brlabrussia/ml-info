import rest_framework_filters as filters
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import viewsets

from other.models import ItunesApp
from other.serializers import ItunesAppSerializer


class ItunesAppFilter(filters.FilterSet):
    class Meta:
        model = ItunesApp
        fields = {
            'created_at': '__all__',
            'updated_at': '__all__',
        }


class ItunesAppViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    """
    Поиск: url, name
    Фильтрация: created_at, updated_at
    """

    serializer_class = ItunesAppSerializer
    queryset = ItunesApp.objects.all()
    ordering = ['-updated_at']
    search_fields = [
        'url',
        'name',
    ]
    filterset_class = ItunesAppFilter
