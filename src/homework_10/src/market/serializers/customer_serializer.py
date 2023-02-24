from typing import Dict

from .user_serializer import user_serializer
from .date_serializer import date_serializer
from .image_serializer import image_serializer


def customer_serializer(customer) -> Dict:
    data = {
        "id": customer.id,
        "user": user_serializer(customer.user),
        "avatar": image_serializer(customer.avatar),
        "registered_at": date_serializer(customer.registered_at)
    }
    return data
