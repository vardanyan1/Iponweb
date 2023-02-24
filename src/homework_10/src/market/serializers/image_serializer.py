def image_serializer(image):
    try:
        return image.url
    except ValueError:
        return "None"
