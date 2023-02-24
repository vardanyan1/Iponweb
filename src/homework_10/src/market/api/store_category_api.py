from rest_framework import viewsets
from ..shop.models.store_category_model import StoreCategory
from ..serializers.serializers import StoreCategorySerializer


class StoreCategoryViewSet(viewsets.ModelViewSet):
    queryset = StoreCategory.objects.all()
    serializer_class = StoreCategorySerializer
