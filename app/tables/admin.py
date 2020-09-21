from django.contrib import admin
from .models import Table, Driver


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    readonly_fields = [
        'result',
    ]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
