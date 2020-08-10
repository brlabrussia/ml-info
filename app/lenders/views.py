from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lender, Loan
from .serializers import (
    BankiSerializer,
    CbrSerializer,
    LenderSerializer,
    LoanSerializer,
    VsezaimyonlineSerializer,
    ZaymovSerializer,
)


class LoanViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LoanSerializer
    queryset = Loan.objects.all()
    search_fields = ('scraped_from', 'name', 'trademark')
    filterset_fields = (
        'lender',
        'amount_max',
        'period_min',
        'period_max',
        'regnum',
        'ogrn',
    )


class LenderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LenderSerializer
    queryset = Lender.objects.all()
    search_fields = ('trademark', 'name', 'full_name')
    filterset_fields = ('is_legal', 'regnum', 'ogrn', 'inn')


class ScrapersView(APIView):
    permission_classes = ()

    def post(self, request, scraper_name):
        if scraper_name == 'cbr':
            serializer_class = CbrSerializer
        elif scraper_name == 'zaymov':
            serializer_class = ZaymovSerializer
        elif scraper_name == 'vsezaimyonline':
            serializer_class = VsezaimyonlineSerializer
        elif scraper_name == 'banki':
            serializer_class = BankiSerializer
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
