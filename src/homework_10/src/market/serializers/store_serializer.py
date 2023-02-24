from .store_owner_serializer import owner_serializer
from .store_category_serializer import store_category_serializer
from typing import Dict


def store_serializer(store) -> Dict:
    data = {
        "id": store.id,
        "name": store.name,
        "owner": owner_serializer(store.owner),
        "store_category": store_category_serializer(store.store_category)}

    return data
