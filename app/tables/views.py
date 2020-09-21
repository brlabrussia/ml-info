from rest_framework import viewsets

from .models import Table
from .serializers import TableSerializer


class TableViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()
