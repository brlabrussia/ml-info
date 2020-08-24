from django.core.validators import integer_validator
from django.db.models import Q
from rest_framework import serializers

from .models import Lender, Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class LenderSerializer(serializers.ModelSerializer):
    loans = LoanSerializer(many=True)

    class Meta:
        model = Lender
        fields = '__all__'


class CbrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = (
            'scraped_from',
            'name_short',
            'name_full',
            'cbr_created_at',
            'type',
            'cbrn',
            'ogrn',
            'inn',
            'website',
            'email',
            'address',
        )
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'cbrn': {'validators': []},
            'ogrn': {'validators': []},
            'inn': {'validators': []},
        }

    def create(self, validated_data):
        # try to find instance in db
        cbrn = validated_data.get('cbrn')
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        qs = Lender.objects.filter(
            Q(cbrn__isnull=False, cbrn=cbrn)
            | Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn),
        )

        # update if found
        if qs.exists():
            return self.update(qs.first(), validated_data)

        # create new if none found
        return Lender.objects.create(
            **validated_data,
            is_legal=True,
        )

    def update(self, instance, validated_data):
        fields_to_override = (
            'name_short',
            'name_full',
            'cbr_created_at',
            'type',
            'cbrn',
            'ogrn',
            'inn',
            'website',
            'email',
            'address',
        )
        updated = False
        for key, value in validated_data.items():
            field_is_empty = not getattr(instance, key)
            want_to_override = key in fields_to_override and value != getattr(instance, key)
            if value and (field_is_empty or want_to_override):
                setattr(instance, key, value)
                updated = True
        if updated:
            instance.save()
        return instance


class ZaymovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = (
            'scraped_from',
            'trademark',
            'logo',
            'cbrn',
            'ogrn',
            'cbr_created_at',
            'address',
        )
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'cbrn': {'validators': []},
            'ogrn': {'validators': []},
        }

    def create(self, validated_data):
        # try to find instance in db
        cbrn = validated_data.get('cbrn')
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        qs = Lender.objects.filter(
            Q(cbrn__isnull=False, cbrn=cbrn)
            | Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn),
        )

        # update if found
        if qs.exists():
            return self.update(qs.first(), validated_data)

        # create new if none found
        return Lender.objects.create(
            **validated_data,
            is_legal=False,
        )

    def update(self, instance, validated_data):
        fields_to_override = (
            'trademark',
            'logo',
            'address',
        )
        updated = False
        for key, value in validated_data.items():
            field_is_empty = not getattr(instance, key)
            want_to_override = key in fields_to_override and value != getattr(instance, key)
            if value and (field_is_empty or want_to_override):
                setattr(instance, key, value)
                updated = True
        if updated:
            if not validated_data['scraped_from'][0] in instance.scraped_from:
                instance.scraped_from += validated_data['scraped_from']
            instance.save()
        return instance


class VsezaimyonlineSerializer(serializers.ModelSerializer):
    """
    url: str
    name: str
    logo: str  # but business don't need such logos
    ogrn: int
    inn: int
    refusal_reasons: List[str]
    social_networks: Optional[List[str]]
    documents: Optional[List[Dict[str, str]]]
    """

    def to_internal_value(self, data):
        return super().to_internal_value({
            'scraped_from': [data.get('url', '')],
            'trademark': data.get('name', ''),
            'ogrn': data.get('ogrn'),
            'inn': data.get('inn'),
            'socials': [
                s for s in data.get('social_networks', [])
                if s.startswith('http') and len(s) < 30
            ],
            'refusal_reasons': data.get('refusal_reasons'),
            'documents': data.get('documents'),
        })

    def create(self, validated_data):
        """
        Can't override `save()` for this class
        since serializer is initiated with `many=True`
        so we implement create/update logic here.
        """

        # dirty fix for very popular company (TODO)
        if validated_data.get('name') == 'Быстроденьги':
            validated_data['ogrn'] = 1087325005899

        # try to find instance in db
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        regnum = validated_data.get('regnum')
        scraped_from = validated_data.get('scraped_from')
        qs = Lender.objects.filter(
            Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn)
            | Q(regnum__isnull=False, regnum=regnum)
            | Q(scraped_from__contains=scraped_from),
        )

        # update if found
        if qs.exists():
            return self.update(qs.first(), validated_data)

        # create new if none found
        return Lender.objects.create(
            **validated_data,
            is_legal=False,
        )

    def update(self, instance, validated_data):
        """
        Only update non-empty fields which have changed.
        We track whether changes have been made so that
        we don't call `save()` for nothing and `updated_at`
        field is meaningful.
        """

        fields_to_override = (
            'trademark',
            'socials',
            'refusal_reasons',
            'documents',
        )
        updated = False
        for key, value in validated_data.items():
            want_to_change = (
                value  # scraped value is non-empty
                and (
                    not getattr(instance, key)  # field is empty
                    or (
                        key in fields_to_override  # we want to override non-empty
                        and value != getattr(instance, key)  # field changed
                    )
                )
            )
            if want_to_change:
                setattr(instance, key, value)
                updated = True
        if updated:
            if not validated_data['scraped_from'][0] in instance.scraped_from:
                instance.scraped_from += validated_data['scraped_from']
            instance.save()
        return instance

    class Meta:
        model = Lender
        fields = (
            'scraped_from',
            'trademark',
            'ogrn',
            'inn',
            'socials',
            'refusal_reasons',
            'documents',
        )
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'ogrn': {'validators': [integer_validator]},
            'inn': {'validators': [integer_validator]},
        }


class BankiSerializer(serializers.ModelSerializer):
    """
    url: str
    name: str
    logo: Optional[str]
    updated_at: str
    loan_purpose: List[str]
    max_money_value: str
    first_loan_condition: Optional[str]
    rate: str
    dates_from: int
    dates_to: int
    loan_time_terms: str
    loan_providing: List[str]
    borrowers_categories: List[str]
    borrowers_age: Optional[str]
    borrowers_registration: List[str]
    borrowers_documents: List[str]
    issuance: str
    loan_processing: List[str]
    loan_form: List[str]
    loan_form_description: Optional[str]
    repayment_order: List[str]
    repayment_order_description: str
    payment_methods: List[str]
    trademark: str
    head_name: Optional[str]
    address: str
    ogrn: Optional[int]
    reg_number: int
    """

    def to_internal_value(self, data):
        return super().to_internal_value({
            'scraped_from': data.get('url', ''),
            'name': data.get('name', ''),
            'last_modified': data.get('updated_at', ''),

            'purpose': data.get('loan_purpose'),
            'amount_max': data.get('max_money_value'),
            'amount_note': data.get('first_loan_condition', ''),
            'rate': data.get('rate', ''),
            'period_min': data.get('dates_from'),
            'period_max': data.get('dates_to'),
            'period_note': data.get('loan_time_terms', ''),
            'collateral': data.get('loan_providing'),

            'borrowers_categories': data.get('borrowers_categories'),
            'borrowers_age': data.get('borrowers_age', ''),
            'borrowers_registration': data.get('borrowers_registration'),
            'borrowers_documents': data.get('borrowers_documents'),

            'issuance': data.get('issuance', ''),
            'loan_processing': data.get('loan_processing'),
            'loan_form': data.get('loan_form'),
            'loan_form_note': data.get('loan_form_description', ''),

            'repayment_order': data.get('repayment_order'),
            'repayment_order_note': data.get('repayment_order_description', ''),
            'payment_methods': data.get('payment_methods'),

            'logo': data.get('logo', ''),
            'trademark': data.get('trademark', ''),
            'address': data.get('address', ''),
            'head_name': data.get('head_name', ''),
            'ogrn': data.get('ogrn'),
            'regnum': data.get('reg_number'),
        })

    def create(self, validated_data):
        """
        Can't override `save()` for this class
        since serializer is initiated with `many=True`
        so we implement create/update logic here.
        """

        # try to find loan
        qs = Loan.objects.filter(scraped_from=validated_data['scraped_from'])

        # update if loan found
        if qs.exists():
            return self.update(qs.first(), validated_data)

        # create new loan if none found
        loan = Loan(**validated_data)

        # try to find lender of our loan
        ogrn = validated_data.get('ogrn')
        regnum = validated_data.get('regnum')
        qs = Lender.objects.filter(
            Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(regnum__isnull=False, regnum=regnum),
        )

        # if found, use id
        if qs.exists():
            lender = qs.first()
            updated = False
            # TODO improve updating
            if not lender.trademark:
                lender.trademark = loan.trademark
                updated = True
            if not lender.head_name:
                lender.head_name = loan.head_name
                updated = True
            if updated:
                lender.scraped_from.append(loan.scraped_from)
                lender.save()
            loan.lender_id = lender.id
        else:
            lender = Lender.objects.create(
                scraped_from=[validated_data['scraped_from']],
                trademark=validated_data['trademark'],
                regnum=validated_data['regnum'],
                ogrn=validated_data['ogrn'],
                address=validated_data['address'],
                is_legal=False,
            )
            loan.lender_id = lender.id

        # TODO logical fields
        # lender.loans.order_by('amount_max')

        loan.save()
        return loan

    def update(self, instance, validated_data):
        """
        Only update non-empty fields which have changed.
        We track whether changes have been made so that
        we don't call `save()` for nothing and `updated_at`
        field is meaningful.
        """

        fields_to_override = (
            'name',
            'last_modified',
            'purpose',
            'amount_max',
            'amount_note',
            'rate',
            'period_min',
            'period_max',
            'period_note',
            'collateral',
            'borrowers_categories',
            'borrowers_age',
            'borrowers_registration',
            'borrowers_documents',
            'issuance',
            'loan_processing',
            'loan_form',
            'loan_form_note',
            'repayment_order',
            'repayment_order_note',
            'payment_methods',
        )
        updated = False
        for key, value in validated_data.items():
            want_to_change = (
                value  # scraped value is non-empty
                and (
                    not getattr(instance, key)  # field is empty
                    or (
                        key in fields_to_override  # we want to override non-empty
                        and value != getattr(instance, key)  # field changed
                    )
                )
            )
            if want_to_change:
                setattr(instance, key, value)
                updated = True
        if updated:
            instance.save()
        return instance

    class Meta:
        model = Loan
        exclude = ('lender',)
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'scraped_from': {'validators': []},
        }
