import banks
import casino
import finance
import insurance
import investments
import mfo
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


class ShareSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = investments.models.Share
        fields = '__all__'


class BondSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = investments.models.Bond
        fields = '__all__'


class IiaSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = investments.models.IIA
        fields = '__all__'


class MutualSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = investments.models.Mutual
        fields = '__all__'


class CompanySerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = insurance.models.Company
        fields = '__all__'


class PersonSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = finance.models.Person
        fields = '__all__'


class DocumentSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = mfo.models.Document
        fields = [
            'name',
            'file',
        ]


class LoanSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = mfo.models.Loan
        fields = '__all__'


class LenderSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    documents = DocumentSerializer(many=True)
    # loans = LoanSerializer(many=True)

    class Meta:
        model = mfo.models.Lender
        exclude = [
            'scraped_from',
            'logo_origin_url',
        ]


class CasinoSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = casino.models.Casino
        fields = '__all__'


class SlotSerializer(FlexFieldsSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = casino.models.Slot
        fields = '__all__'
