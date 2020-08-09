from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Lender, Loan
from .serializers import CbrSerializer, LenderSerializer, LoanSerializer


class CbrView(APIView):
    permission_classes = []

    def post(self, request):
        serializer = CbrSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
