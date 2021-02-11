from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers

from banks.models import Rating


class RatingSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
