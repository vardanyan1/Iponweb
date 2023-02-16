from django.urls import path
from .api.item_category import ItemsCategoryView


urlpatterns = [
    path('item_category', ItemsCategoryView.as_view()),
    path("item_category/<int:id>", ItemsCategoryView.check_view)
]
