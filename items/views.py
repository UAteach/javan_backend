from rest_framework import generics, permissions

from .models import Item
from .serializers import ItemSerializer

class ListItem(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class Item(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer