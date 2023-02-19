"""market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .api.items_category_api import ItemsCategoryView
from .api.store_category_api import StoreCategoryView
from .api.store_owner_api import StoreOwnerView
from .api.store_api import StoreView
from .api.customer_api import CustomerView
from .api.item_api import ItemView
from .api.my_bag_api import MyBagView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/items_category', ItemsCategoryView.as_view()),
                  path("api/items_category/<int:id>", ItemsCategoryView.check_view),
                  path('api/store_category', StoreCategoryView.as_view()),
                  path("api/store_category/<int:id>", StoreCategoryView.check_view),
                  path('api/store_owner', StoreOwnerView.as_view()),
                  path('api/store_owner/<int:id>', StoreOwnerView.check_view),
                  path('api/store', StoreView.as_view()),
                  path('api/store/<int:id>', StoreView.check_view),
                  path('api/customer', CustomerView.as_view()),
                  path('api/customer/<int:id>', CustomerView.check_view),
                  path('api/item', ItemView.as_view()),
                  path('api/item/<int:id>', ItemView.check_view),
                  path('api/my_bag', MyBagView.as_view()),
                  path('api/my_bag/<int:id>', MyBagView.check_view),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
