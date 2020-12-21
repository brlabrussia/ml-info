from rest_framework import viewsets

from investments.models import IIA, Bond, Mutual, Share
from investments.serializers import (
    BondSerializer,
    IIASerializer,
    MutualSerializer,
    ShareSerializer,
)


class ShareViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShareSerializer
    queryset = Share.objects.all()


class BondViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BondSerializer
    queryset = Bond.objects.all()


class IIAViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = IIASerializer
    queryset = IIA.objects.all()


class MutualViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MutualSerializer
    queryset = Mutual.objects.all()
