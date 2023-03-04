from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action

from ..shop.models.items_category_model import ItemsCategory
from ..shop.models.item_model import Item
from ..serializers.serializers import ItemCategorySerializer, ItemSerializer


class ItemCategoryViewSet(viewsets.ModelViewSet):
    queryset = ItemsCategory.objects.all()
    serializer_class = ItemCategorySerializer

    @action(detail=True, url_name='item_category_items')
    def items(self, request, pk=None):
        item_category = self.get_object()
        queryset = Item.objects.filter(category_id=item_category)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)
