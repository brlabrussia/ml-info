from common.utils import ExportCsvMixin
from django.contrib import admin

from investments.models import Share


class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']


@admin.register(Share)
class ShareAdmin(BaseAdmin):
    list_display = [
        'isin',
        'name',
        'price',
    ]
