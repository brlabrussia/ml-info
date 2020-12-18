from rest_framework import viewsets

from investments.models import Bond, Share
from investments.serializers import BondSerializer, ShareSerializer


class ShareViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShareSerializer
    queryset = Share.objects.all()


class BondViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BondSerializer
    queryset = Bond.objects.all()
