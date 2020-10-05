from django.contrib import admin

from .models import Driver, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    readonly_fields = [
        'result',
    ]

    list_display = [
        'name',
        'url',
        'description',
        'category',
        'driver',
    ]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
