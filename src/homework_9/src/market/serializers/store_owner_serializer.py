from .user_serializer import user_serializer
from .date_serializer import date_serializer
from .image_serializer import image_serializer


def owner_serializer(owner):
    data = {
        "id": owner.id,
        "user": user_serializer(owner.user),
        "avatar": image_serializer(owner.avatar),
        "registered_at": date_serializer(owner.registered_at)
        }

    return data
