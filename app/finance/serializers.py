from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers

from finance.models import Person


class PersonSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
