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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.routers import SimpleRouter
from .api.customer_api import CustomerViewSet
from .api.items_category_api import ItemCategoryViewSet
from .api.item_api import ItemViewSet
from .api.registration_api import RegistrationView
from .api.store_category_api import StoreCategoryViewSet
from .api.store_owner_api import StoreOwnerViewSet
from .api.store_api import StoreViewSet
from .api.my_bag_api import MyBagViewSet
from .api.purchase_api import PurchaseViewSet

urlpatterns = [

                  path('api/auth/login/', RegistrationView.login, name='login'),
                  path('api/auth/register/', RegistrationView.register, name='register'),
                  path('api/auth/logout/', RegistrationView.logout, name='logout'),
                  path('api/auth/refresh-token/', RegistrationView.refresh_token, name='refresh_token'),
                  path('api/auth/send_verification_code/<int:user_id>/', RegistrationView.send_verification_code,
                       name='send_verification_code'),
                  path('api/auth/verify/', RegistrationView.verify, name='verify_user'),
                  path('admin/', admin.site.urls),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router = SimpleRouter()
router.register("api/customer", CustomerViewSet, "customer")
router.register("api/item_category", ItemCategoryViewSet, "item_category")
router.register("api/store_category", StoreCategoryViewSet, "store_category")
router.register("api/store_owner", StoreOwnerViewSet, "store_owner")
router.register("api/item", ItemViewSet, "item")
router.register("api/store", StoreViewSet, "store")
router.register("api/my_bag", MyBagViewSet, "my_bag")
router.register("api/purchase", PurchaseViewSet, "purchase")

urlpatterns += router.urls

urlpatterns += staticfiles_urlpatterns()
