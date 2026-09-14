from django.urls import path

from orders.views import get_orders, get_items



urlpatterns = [
    path('orders/', get_orders, name='order_list'),
    path('items/<int:id>/', get_items, name='item_list'),
]