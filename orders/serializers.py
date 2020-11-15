from rest_framework import serializers
from .models import Order, OrderContent, OrderComplete
from core.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    members = UserSerializer(read_only=True, many=True)
    class Meta:
        fields = '__all__'
        model = Order
    # class Meta:
    #     fields = (
    #         'id',
    #         'bin_number',
    #         'status',
    #         'master_teacher',
    #         'members',
    #         'trello_id',
    #         'expected_pickup_datetime',
    #         'actual_pickup_datetime',
    #         'expected_return_datetime',
    #         'actual_return_datetime',
    #         'other_notes'
    #     )
    #     model = Order


class OrderContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'order',
            'item',
            'name',
            'quantity',
            'other_notes',
            'self_filled'
        )
        model = OrderContent

