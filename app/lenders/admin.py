from django.contrib import admin

from lenders.models import Lender, Loan

admin.site.register(Lender)
admin.site.register(Loan)
