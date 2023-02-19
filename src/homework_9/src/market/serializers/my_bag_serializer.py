from typing import Dict
from .customer_serializer import customer_serializer
from .item_serializer import item_serializer


def my_bag_serializer(bag) -> Dict:
    data = {
        "id": bag.id,
        "customer": customer_serializer(bag.customer),
        "items": [item_serializer(item) for item in bag.items.all()],
        "total_price": str(bag.total_price)
    }

    return data
