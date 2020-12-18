from common.utils import ExportCsvMixin
from django.contrib import admin

from investments.models import Bond, Share


@admin.register(Bond, Share)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
