from django.contrib import admin

from .models import Lender, Loan

admin.site.register(Loan)


class LoanInline(admin.TabularInline):
    model = Loan
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
    inlines = [LoanInline]
