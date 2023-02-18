from .user_serializer import user_serializer


def owner_serializer(owner):
    data = {"user": user_serializer(owner.user), "avatar": owner.avatar.url,
            "registered_at": owner.registered_at.strftime('%Y-%m-%d')}

    return data
