from typing import Dict
from .image_serializer import image_serializer


def item_category_serializer(item_category) -> Dict:
    data = {
        "id": item_category.id,
        "name": item_category.name,
        "photo": image_serializer(item_category.photo)
        }

    return data
