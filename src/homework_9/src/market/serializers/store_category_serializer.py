def store_category_serializer(store_category):
    data = {
        "id": store_category.id,
        "name": store_category.name
    }

    return data
