from .views import PostViewSet, UserViewSet
from rest_framework.routers import SimpleRouter
from django.urls import path

router = SimpleRouter()
router.register("users", UserViewSet, "users")
router.register("", PostViewSet, "posts")

urlpatterns = router.urls
