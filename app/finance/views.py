import rest_framework_filters as filters
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import viewsets

from finance.models import Person
from finance.serializers import PersonSerializer


class PersonFilter(filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            'created_at': '__all__',
            'updated_at': '__all__',
        }


class PersonViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    ordering = ['-updated_at']
    filterset_class = PersonFilter
