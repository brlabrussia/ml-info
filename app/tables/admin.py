from django.contrib import admin

from .models import Driver, Table


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    readonly_fields = [
        'result',
        'updated_at',
        'created_at',
    ]

    list_display = [
        'name',
        'url',
        'category',
        'driver',
    ]

    search_fields = [
        'name',
        'url',
    ]

    list_filter = [
        'category',
        'driver',
    ]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
