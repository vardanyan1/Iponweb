from django.views.generic import View
from market.market.shop.models import StoreCategory


class StoreCategoryView(View):
    @staticmethod
    def get(request):
        categories = StoreCategory.objects.all()
