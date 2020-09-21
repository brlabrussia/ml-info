from rest_framework import serializers

from .models import Table


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        exclude = [
            'driver',
            'driver_args',
        ]
