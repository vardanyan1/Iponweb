def item_category_serializer(item_category):
    data = {
        "id": item_category.id,
        "name": item_category.name
        }

    return data
