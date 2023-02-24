from typing import Dict
from .customer_serializer import customer_serializer
from .item_serializer import item_serializer
from .date_serializer import date_serializer


def purchase_serializer(purchase) -> Dict:
    data = {
        "id": purchase.id,
        "items": [item_serializer(item) for item in purchase.items.all()],
        "buy_time": date_serializer(purchase.buy_time),
        "customer": customer_serializer(purchase.customer),
        "total_price": str(purchase.total_price)
    }

    return data
