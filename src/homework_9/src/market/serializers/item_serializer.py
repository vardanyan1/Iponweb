from typing import Dict
from ..serializers.image_serializer import image_serializer
from ..serializers.item_category_serializer import item_category_serializer
from ..serializers.store_serializer import store_serializer


def item_serializer(item) -> Dict:
    data = {
        "id": item.id,
        "name": item.name,
        "picture": image_serializer(item.picture),
        "item_category": item_category_serializer(item.category),
        "price": str(item.price),
        "quantity": str(item.quantity),
        "info": item.info,
        "store": store_serializer(item.store)

    }

    return data
