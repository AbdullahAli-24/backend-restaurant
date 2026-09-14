
from rest_framework.response import Response
from .serializers import OrderSerializer, ItemsOrderSerializer
from .models import Order, Items_Order
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_items(request, id):
    items = Items_Order.objects.get(id=id)
    serializer = ItemsOrderSerializer(items)
    return Response(serializer.data)