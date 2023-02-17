from django.views.generic import View
from market.market.shop.models.store_category_model import StoreCategory
from market.market.tools.sending_tools import data_status


class StoreCategoryView(View):
    @staticmethod
    def get(request):
        categories = StoreCategory.objects.all()
        data = []
        for category in categories:
            data.append({"name": category.name, "id": category.id})

        return data_status(data=data)
