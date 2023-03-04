from rest_framework import viewsets
from ..shop.models.store_model import Store
from ..serializers.serializers import StoreSerializer


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
