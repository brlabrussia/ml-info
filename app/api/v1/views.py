import banks
from api.v1 import serializers
from rest_flex_fields.views import FlexFieldsMixin
from rest_framework import viewsets


class BankViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BankSerializer
    queryset = banks.models.Bank.objects.all()
    ordering = ['-updated_at']


class DebitCardViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DebitCardSerializer
    queryset = banks.models.DebitCard.objects.all()
    ordering = ['-updated_at']


class CreditCardViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CreditCardSerializer
    queryset = banks.models.CreditCard.objects.all()
    ordering = ['-updated_at']


class AutoCreditViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AutoCreditSerializer
    queryset = banks.models.AutoCredit.objects.all()
    ordering = ['-updated_at']


class ConsumerCreditViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ConsumerCreditSerializer
    queryset = banks.models.ConsumerCredit.objects.all()
    ordering = ['-updated_at']


class DepositViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.DepositSerializer
    queryset = banks.models.Deposit.objects.all()
    ordering = ['-updated_at']


class BranchViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BranchSerializer
    queryset = banks.models.Branch.objects.all()
    ordering = ['-updated_at']


class RatingViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.RatingSerializer
    queryset = banks.models.Rating.objects.all()
    ordering = ['-updated_at']
