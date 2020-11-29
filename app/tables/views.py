from django.shortcuts import render
from rest_framework import mixins, viewsets

from .models import Table
from .serializers import TableSerializer


def preview(request, id):
    table = Table.objects.get(id=id)
    return render(request, 'preview.html', {'table': table})


class TableViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
