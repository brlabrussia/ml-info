from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Table
from .serializers import TableSerializer


class TableViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TableSerializer
    queryset = Table.objects.all()


class ScrapersView(APIView):
    permission_classes = ()

    def post(self, request):
        pk = request.data.get('instance_id')
        table = Table.objects.get(pk=pk)
        table.result = request.data.get('result')
        table.save()
        return Response(status.HTTP_202_ACCEPTED)
