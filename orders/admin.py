from django.contrib import admin
from .models import Order, OrderContent


class OrderAdmin(admin.ModelAdmin):
    list_display = ('bin_number', 'status', 'master_teacher', 
                    'trello_id', 'expected_pickup_datetime', 'actual_pickup_datetime', 
                    'expected_return_datetime', 'actual_return_datetime', 'other_notes')


class OrderContentAdmin(admin.ModelAdmin):
    list_display = ('order', 'quantity', 'item')


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderContent, OrderContentAdmin)
