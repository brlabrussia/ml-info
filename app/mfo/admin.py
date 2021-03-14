from django.contrib import admin

from .models import Document, Lender, Loan


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0


@admin.register(Lender)
class LenderAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created_at',
        'updated_at',
        'amount_min',
        'amount_max',
        'overpayment_day',
        'overpayment_full',
    ]
    inlines = [DocumentInline]


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    readonly_fields = [
        'created_at',
        'updated_at',
    ]
