
from .models import Order, Items_Order
from rest_framework import serializers

from foods.serializers import FoodSerializer


class ItemsOrderSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)
    class Meta:
        model = Items_Order
        fields = ['food','quantity','id','total_price']

    def create(self, validated_data):
        return Items_Order.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.save()
        return instance

    
class OrderSerializer(serializers.ModelSerializer):
    items=ItemsOrderSerializer(many=True,read_only=True)
    class Meta:
        model = Order
        fields = ['items','id','user']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
