from typing import Dict
from .image_serializer import image_serializer


def store_category_serializer(store_category) -> Dict:
    data = {
        "id": store_category.id,
        "name": store_category.name,
        "photo": image_serializer(store_category.photo)
    }

    return data
