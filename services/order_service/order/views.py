from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
import requests


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=["GET"], detail=True, url_path="details")
    def get_order_details(self, request, pk=None):
        order = get_object_or_404(self.queryset, pk=pk)
        order_details = requests.get(
            f"http://localhost:8005/api/v1/carts/{order.cart_id}"
        ).json()
        response = {
            "order": OrderSerializer(order).data,
            "order_details": order_details,
        }
        return Response(
            data=response, status=status.HTTP_200_OK, content_type="application/json"
        )

    @action(methods=["GET"], detail=False, url_path="users/(?P<user_id>.+)")
    def get_orders_by_user_id(self, request, user_id=None):
        carts = requests.get(
            f"http://localhost:8005/api/v1/carts/users/{user_id}"
        ).json()
        response = []
        ok = False
        for cart in carts:
            if cart.get("cart").get("status"):
                order = Order.objects.filter(cart_id=cart.get("cart").get("id")).get()
                data = {"order": OrderSerializer(order).data, "details": cart}
                response.append(data)
                ok = True

        if ok:
            return Response(
                data=response,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(
                data={"message": f"There is no orders with user ID {user_id}"},
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json",
            )
