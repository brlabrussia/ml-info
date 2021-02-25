import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import (
    AutoCredit,
    Bank,
    Branch,
    ConsumerCredit,
    CreditCard,
    DebitCard,
    Deposit,
    Rating,
)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [
            field.name if not field.is_relation else field.name + '_id'
            for field in meta.fields
        ]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response


@admin.register(
    AutoCredit,
    Branch,
    ConsumerCredit,
    CreditCard,
    DebitCard,
    Deposit,
    Rating,
)
class BankAdditionalAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ['name']
    actions = ['export_as_csv']


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin, ExportCsvMixin):
    search_fields = ['full_name', 'name', 'english_name']
    actions = ['export_as_csv']
