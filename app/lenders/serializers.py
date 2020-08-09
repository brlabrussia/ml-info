import django
from django.core.validators import integer_validator
from django.db.models import Q
from rest_framework import serializers

from .models import Lender, Loan


class LenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lender
        fields = '__all__'


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'


class CbrSerializer(serializers.ModelSerializer):
    """
    name: str
    full_name: str
    mfo_type: str
    registry_date: str
    reg_number: int
    ogrn: int
    inn: int
    url: str
    email: str
    address: str
    """

    def to_internal_value(self, data):
        return super().to_internal_value({
            'name': data.get('name', ''),
            'full_name': data.get('full_name', ''),
            'type': data.get('mfo_type', ''),
            'regdate': data.get('registry_date'),
            'regnum': data.get('reg_number'),
            'ogrn': data.get('ogrn'),
            'inn': data.get('inn'),
            'website': self.format_website(data.get('url', '')),
            'email': self.format_email(data.get('email', '')),
            'address': data.get('address', ''),
        })

    def format_website(self, value):
        # multiple websites separated by comma or semicolon
        value.replace(', ', ';')
        if len(value.split(';')) != 1:
            value = value.split(';')[0]
        # no protocol
        if value and not value.startswith('http'):
            value = 'http://' + value
        # Give up if nothing works (TODO)
        try:
            django.core.validators.URLValidator()(value)
        except django.core.exceptions.ValidationError:
            value = ''
        return value

    def format_email(self, value):
        # multiple emails separated by comma or semicolon
        value.replace(', ', ';')
        if len(value.split(';')) != 1:
            value = value.split(';')[0]
        # Give up if nothing works (TODO)
        try:
            django.core.validators.EmailValidator()(value)
        except django.core.exceptions.ValidationError:
            value = ''
        return value

    def create(self, validated_data):
        """
        Can't override `save()` for this class
        since serializer is initiated with `many=True`
        so we implement create/update logic here.
        """

        # try to find instance in db
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        regnum = validated_data.get('regnum')
        qs = Lender.objects.filter(
            Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn)
            | Q(regnum__isnull=False, regnum=regnum),
        )

        # update if found
        if qs.exists():
            return self.update(qs.first(), validated_data)

        # create new if none found
        return Lender.objects.create(
            **validated_data,
            scraped_from=['https://www.cbr.ru/vfs/finmarkets/files/supervision/list_MFO.xlsx'],
            is_legal=True,
        )

    def update(self, instance, validated_data):
        """
        Only update non-empty fields which have changed.
        We track whether changes have been made so that
        we don't call `save()` for nothing and `updated_at`
        field is meaningful.
        """

        fields_to_override = (
            'name',
            'full_name',
            'type',
            'regdate',
            'regnum',
            'ogrn',
            'inn',
            # 'website',
            # 'email',
            'address',
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
        model = Lender
        fields = (
            'name',
            'full_name',
            'type',
            'regdate',
            'regnum',
            'ogrn',
            'inn',
            'website',
            'email',
            'address',
        )
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'ogrn': {'validators': [integer_validator]},
            'inn': {'validators': [integer_validator]},
            'regnum': {'validators': [integer_validator]},
        }


class ZaymovSerializer(serializers.ModelSerializer):
    """
    url: str
    name: str
    logo: str
    reg_number: int
    ogrn: int
    address: str
    """

    def to_internal_value(self, data):
        return super().to_internal_value({
            'scraped_from': [data.get('url', '')],
            'trademark': data.get('name', ''),
            'logo': data.get('logo', ''),
            'regnum': data.get('reg_number'),
            'ogrn': data.get('ogrn'),
            'address': data.get('address', ''),
        })

    def create(self, validated_data):
        """
        Can't override `save()` for this class
        since serializer is initiated with `many=True`
        so we implement create/update logic here.
        """

        # try to find instance in db
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        regnum = validated_data.get('regnum')
        qs = Lender.objects.filter(
            Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn)
            | Q(regnum__isnull=False, regnum=regnum),
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
            'logo',
            'address',
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
            'logo',
            'regnum',
            'ogrn',
            'address',
        )
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'ogrn': {'validators': [integer_validator]},
            'regnum': {'validators': [integer_validator]},
        }


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

        # try to find instance in db
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        regnum = validated_data.get('regnum')
        qs = Lender.objects.filter(
            Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn)
            | Q(regnum__isnull=False, regnum=regnum),
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
