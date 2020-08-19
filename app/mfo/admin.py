from django.contrib import admin

from .models import Lender, Loan

admin.site.register(Lender)
admin.site.register(Loan)
