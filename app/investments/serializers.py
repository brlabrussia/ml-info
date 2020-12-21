from rest_framework import serializers

from investments.models import IIA, Bond, Share


class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = '__all__'


class BondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = '__all__'


class IIASerializer(serializers.ModelSerializer):
    class Meta:
        model = IIA
        fields = '__all__'
