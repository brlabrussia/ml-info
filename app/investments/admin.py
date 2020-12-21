from common.utils import ExportCsvMixin
from django.contrib import admin

from investments.models import IIA, Bond, Mutual, Share


@admin.register(IIA, Bond, Mutual, Share)
class BaseAdmin(ExportCsvMixin, admin.ModelAdmin):
    actions = ['export_as_csv']
