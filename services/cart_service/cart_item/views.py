from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer


# Create your views here.
class CartItemViewSet(viewsets.ViewSet):

    def create(self, request):
        post_data = request.data
        serializer = CartItemSerializer(data=post_data)
        if serializer.is_valid():
            cart_id = post_data.get("cart")
            category_id = post_data.get("category_id")
            product_id = post_data.get("product_id")
            quantity = post_data.get("quantity")
            cart_items = CartItem.objects.filter(cart_id=cart_id)
            book_in_cart = False
            for cart_item in cart_items:
                if (
                    int(cart_item.category_id) == category_id
                    and int(cart_item.product_id) == product_id
                ):
                    cart_item.augment_quantity(quantity=quantity)
                    print("Da vao")
                    book_in_cart = True
                    break

            if not book_in_cart:
                serializer.save()

            return Response(
                data={"message": "Add item to cart successfully."},
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(serializer.errors, status=400)

    def update(self, request, pk=None):
        update_data = request.data
        cart_item = CartItem.objects.filter(pk=pk).get()
        serializer = CartItemSerializer(cart_item, data=update_data)
        if serializer.is_valid():
            quantity = update_data.get("quantity")
            if cart_item:
                if int(quantity) > 0:
                    cart_item.quantity = quantity
                    cart_item.save()
                    return Response(
                        data={"message": "Update item in cart successfully."},
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
                else:
                    return Response(
                        data={"message": "Quantity must be greater than 0."},
                        status=status.HTTP_400_BAD_REQUEST,
                        content_type="application/json",
                    )
            else:
                return Response(
                    data={"message": "Item not found."},
                    status=status.HTTP_400_BAD_REQUEST,
                    content_type="application/json",
                )
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        cart_item = CartItem.objects.filter(pk=pk).get()
        if cart_item:
            cart_item.delete()
            return Response(
                data={"message": "Delete item in cart successfully."},
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        else:
            return Response(
                data={"message": "Item not found."},
                status=status.HTTP_204_NO_CONTENT,
                content_type="application/json",
            )
