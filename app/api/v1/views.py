import banks
import casino
import finance
import insurance
import investments
import mfo
import rankings
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


class ShareViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.ShareSerializer
    queryset = investments.models.Share.objects.all()
    ordering = ['-updated_at']


class BondViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BondSerializer
    queryset = investments.models.Bond.objects.all()
    ordering = ['-updated_at']


class IiaViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.IiaSerializer
    queryset = investments.models.IIA.objects.all()
    ordering = ['-updated_at']


class MutualViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MutualSerializer
    queryset = investments.models.Mutual.objects.all()
    ordering = ['-updated_at']


class CompanyViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CompanySerializer
    queryset = insurance.models.Company.objects.all()
    ordering = ['-updated_at']


class PersonViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.PersonSerializer
    queryset = finance.models.Person.objects.all()
    ordering = ['-updated_at']


class LoanViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.LoanSerializer
    queryset = mfo.models.Loan.objects.all()
    ordering = ['-updated_at']


class LenderViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.LenderSerializer
    queryset = mfo.models.Lender.objects.all()
    ordering = ['-updated_at']


class CasinoViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CasinoSerializer
    queryset = casino.models.Casino.objects.all()
    ordering = ['-updated_at']


class SlotViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.SlotSerializer
    queryset = casino.models.Slot.objects.all()
    ordering = ['-updated_at']


class RankingViewSet(FlexFieldsMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.RankingSerializer
    queryset = rankings.models.Ranking.objects.all()
    ordering = ['-updated_at']
