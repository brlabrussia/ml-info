from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers

from other.models import ItunesApp


class ItunesAppSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ItunesApp
        fields = '__all__'
