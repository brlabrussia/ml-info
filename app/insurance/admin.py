from common.utils import ExportCsvMixin
from django.contrib import admin

from insurance.models import Company


@admin.register(Company)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
