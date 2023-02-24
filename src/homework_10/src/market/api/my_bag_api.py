from rest_framework import viewsets
from ..shop.models.my_bag_model import MyBag
from ..serializers.serializers import MyBagSerializer


class MyBagViewSet(viewsets.ModelViewSet):
    queryset = MyBag.objects.all()
    serializer_class = MyBagSerializer
