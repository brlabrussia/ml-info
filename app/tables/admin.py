from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Driver, Table
from .tasks import schedule_scraper


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    readonly_fields = [
        'updated_at',
        'created_at',
    ]

    exclude = [
        'result',
    ]

    list_display = [
        'preview',
        'name',
        'url',
        'category',
        'driver',
    ]

    list_display_links = [
        'name',
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

    @mark_safe
    def preview(self, obj):
        return '<a class="button" href="{}">Preview</a>'.format(
            reverse('preview', args=[obj.pk]),
        )

    def schedule(self, request, queryset):
        for obj in queryset:
            schedule_scraper.delay(
                obj.driver.scraper,
                obj.pk,
                obj.url,
                obj.driver_args,
            )
    schedule.short_description = 'Schedule selected tables'
    schedule.allowed_permissions = ['delete']


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
