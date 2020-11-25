from django.contrib import admin

from .models import Driver, Table
from .tasks import schedule_scraper


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

    actions = [
        'schedule',
    ]

    def schedule(self, request, queryset):
        for obj in queryset:
            schedule_scraper.delay(
                obj.driver.scraper,
                obj.pk,
                obj.url,
                obj.driver_args,
            )
    schedule.short_description = 'Schedule selected tables'


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
