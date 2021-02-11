from common.utils import ExportCsvMixin
from django.contrib import admin

from finance import models


@admin.register(models.Person)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
