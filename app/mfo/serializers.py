from collections import OrderedDict

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
    class Meta:
        model = Lender
        fields = (
            'scraped_from',
            'trademark',
            'ogrn',
            'inn',
            'decline_reasons',
            'socials',
            'documents',
            'decision_speed',
            'payment_speed',
        )
        extra_kwargs = {
            # following fields have `unique=True` constraint
            # disable `UniqueValidator` since we manage it in `create()`
            'ogrn': {'validators': []},
            'inn': {'validators': []},
        }

    def create(self, validated_data):
        # dirty fix for very popular company (TODO)
        if validated_data.get('trademark') == 'Быстроденьги':
            validated_data['ogrn'] = '1087325005899'

        # try to find instance in db
        ogrn = validated_data.get('ogrn')
        inn = validated_data.get('inn')
        scraped_from = validated_data.get('scraped_from')
        qs = Lender.objects.filter(
            Q(ogrn__isnull=False, ogrn=ogrn)
            | Q(inn__isnull=False, inn=inn)
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
        fields_to_override = (
            'trademark',
            'decline_reasons',
            'socials',
            'documents',
            'decision_speed',
            'payment_speed',
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
