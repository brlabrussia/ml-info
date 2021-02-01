from common.utils import ExportCsvMixin
from django.contrib import admin

from other.models import ItunesApp


@admin.register(ItunesApp)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
