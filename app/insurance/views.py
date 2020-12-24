from rest_framework import viewsets

from insurance.models import Company
from insurance.serializers import CompanySerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
