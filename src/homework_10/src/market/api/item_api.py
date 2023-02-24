from rest_framework import viewsets
from ..shop.models.item_model import Item
from ..serializers.serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
