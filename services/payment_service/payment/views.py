from rest_framework.decorators import action
from .models import Payment

# from shipment_update.views import shipment_details_update as ship_update
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    @action(methods=["GET"], detail=False, url_path="users/(?P<user_id>.+)")
    def get_transactions_by_user_id(self, request, user_id=None):
        payments = Payment.objects.filter(user_id=user_id)
        response = PaymentSerializer(payments, many=True)
        return Response(data=response.data)
