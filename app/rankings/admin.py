from common.utils import ExportCsvMixin
from django.contrib import admin

from rankings import models


@admin.register(
    models.Ranking,
)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
