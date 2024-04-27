from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from cart.models import Cart
from cart_item.models import CartItem
from decimal import Decimal
import requests
from .serializers import CartSerializer
from cart_item.serializers import CartItemSerializer
# Create your views here.
class CartViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        cart = get_object_or_404(Cart.objects.all(), pk=pk)
        cart_items = CartItem.objects.filter(cart=cart)
        cart_total = Decimal("0.00")
        product_details ={}
        for cart_item in cart_items:
            if int(cart_item.category_id) == 1:
                response = requests.get(
                    f"http://localhost:8002/api/v1/books/{cart_item.product_id}/"
                ).json()
                cart_total += cart_item.quantity * Decimal(response.get("price"))
            elif int(cart_item.category_id) == 2:
                response = requests.get(
                    f"http://localhost:8003/api/v1/clothes/{cart_item.product_id}/"
                ).json()
                cart_total += cart_item.quantity * Decimal(response.get("price"))
            elif int(cart_item.category_id) == 3:
                response = requests.get(
                    f"http://localhost:8004/api/v1/mobiles/{cart_item.product_id}/"
                ).json()
                cart_total += cart_item.quantity * Decimal(response.get("price"))
            product_details[cart_item.product_id+"_"+cart_item.category_id] = response
        response = {
            "cart": CartSerializer(cart).data,
            "items": CartItemSerializer(cart_items, many=True).data,
            "total": cart_total,
            "product_details": product_details,
        }
        return Response(
            data=response,
            status=status.HTTP_200_OK,
            content_type="application/json",
        )

    @action(methods=["GET"], detail=False, url_path="users/(?P<user_id>.+)")
    def get_carts_by_user_id(self, request, user_id=None):
        carts = Cart.objects.filter(user_id=user_id)
        response = []
        ok = False
        for cart in carts:
            cart_details = self.retrieve(request=request, pk=cart.pk).data
            response.append(cart_details)
            ok = True
        if ok:
            return Response(
                data=response,
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(
                data={"message": f"There is no carts with user ID {user_id}"},
                status=status.HTTP_400_BAD_REQUEST,
                content_type="application/json",
            )

    def create(self, request):
        cart = CartSerializer(data=request.data)
        if cart.is_valid():
            cart.save()
            return Response(cart.data, status=201)
        else:
            return Response(cart.errors, status=400)

    def update(self, request, pk=None):
        cart = Cart.objects.filter(pk=pk).get()
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={"message": "Update cart successfully."},
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        cart = Cart.objects.filter(pk=pk).get()
        if cart:
            cart.delete()
            return Response(
                data={"message": "Delete cart successfully."},
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(
                data={"message": "Cart not found."},
                status=status.HTTP_204_NO_CONTENT,
                content_type="application/json",
            )
