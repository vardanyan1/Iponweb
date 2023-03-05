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
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .api.customer_api import CustomerViewSet
from .api.items_category_api import ItemCategoryViewSet
from .api.item_api import ItemViewSet
from .api.store_category_api import StoreCategoryViewSet
from .api.store_owner_api import StoreOwnerViewSet
from .api.store_api import StoreViewSet
from .api.my_bag_api import MyBagViewSet
from .api.purchase_api import PurchaseViewSet
from .api.user_api import RegisterView, VerificationView, ChangePasswordView, LogoutView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/auth/register/', RegisterView.as_view(), name='auth_register'),
                  path('api/auth/verify/', VerificationView.as_view(), name='verify_user'),
                  path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/auth/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
                  path('api/auth/logout/', LogoutView.as_view(), name='auth_logout'),
                  path('api/auth/change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

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
