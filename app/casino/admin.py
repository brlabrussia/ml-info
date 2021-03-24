from common.utils import ExportCsvMixin
from django.contrib import admin

from casino import models


@admin.register(
    models.Casino,
    models.Slot,
)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
