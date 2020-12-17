from rest_framework import viewsets

from investments.models import Share
from investments.serializers import ShareSerializer


class ShareViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ShareSerializer
    queryset = Share.objects.all()
