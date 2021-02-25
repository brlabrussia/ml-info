import banks
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework import serializers


class BankSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.Bank
        fields = '__all__'


class DebitCardSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.DebitCard
        fields = '__all__'


class CreditCardSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.CreditCard
        fields = '__all__'


class AutoCreditSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.AutoCredit
        fields = '__all__'


class ConsumerCreditSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.ConsumerCredit
        fields = '__all__'


class DepositSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.Deposit
        fields = '__all__'


class BranchSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.Branch
        fields = '__all__'


class RatingSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = banks.models.Rating
        fields = '__all__'
