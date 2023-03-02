from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

from ..shop.models.store_owner_model import StoreOwner
from ..serializers.serializers import StoreOwnerSerializer


class StoreOwnerViewSet(viewsets.ModelViewSet):
    queryset = StoreOwner.objects.all()
    serializer_class = StoreOwnerSerializer

    def partial_update(self, request, *args, **kwargs):
        raise MethodNotAllowed('PATCH')
