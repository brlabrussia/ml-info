from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Table
from .tasks import schedule_spider


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
        'url_as_link',
        'category',
        'spider',
        'spider_kwargs',
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
        'spider',
    ]

    actions = [
        'schedule',
    ]

    @mark_safe
    def url_as_link(self, obj) -> str:
        return f'<a href="{obj.url}">{obj.url}</a>'
    url_as_link.short_description = 'Url'

    @mark_safe
    def preview(self, obj) -> str:
        return '<a class="button" href="{}">Preview</a>'.format(
            reverse('preview', args=[obj.pk]),
        )

    def schedule(self, request, queryset) -> None:
        for obj in queryset:
            if obj.url and obj.spider:
                schedule_spider.delay(
                    obj.pk,
                    obj.url,
                    obj.spider,
                    obj.spider_kwargs,
                )
    schedule.short_description = 'Schedule selected tables'
    schedule.allowed_permissions = ['delete']
